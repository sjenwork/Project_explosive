import sys
import traceback

def getError(e):
    error_class = e.__class__.__name__  # 取得錯誤類型
    detail = e.args[0]  # 取得詳細內容

    _, _, tb = sys.exc_info()  # 取得Call Stack
    lastCallStack = traceback.extract_tb(tb)  # 取得Call Stack的最後一筆資料
    print('--')
    print('Traceback:')
    for ierr in lastCallStack:
        fileName = ierr[0]  # 取得發生的檔案名稱
        lineNum = ierr[1]  # 取得發生的行號
        funcName = ierr[2]  # 取得發生的函數名稱
        if (fileName != '<string>') and (fileName[-2:] == 'py'):
            with open(fileName) as f:
                errCode = f.readlines()[lineNum-1].strip()
        else:
            errCode = "    can't get error code by exec reading"
        errMsg = f'''  File "{fileName}", line {lineNum}, in {funcName}\n    {errCode}'''
        print(errMsg)
        # print('--')
    print(f'{error_class}: {detail}')
    print('--')