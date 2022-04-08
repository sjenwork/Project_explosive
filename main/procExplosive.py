import pathlib
from textwrap import indent
from sqlalchemy import create_engine
import sqlalchemy
import copy
import geopandas as gpd
import re
import pandas as pd
from src.sql_tools import get_conn as connSQL, insert, table_check, fetchall
from src.mongo_tools import get_conn as connMongo
import json
import numpy as np
import os
import pymongo


pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.unicode.ambiguous_as_wide', True)


# 將原始檔案整理好後寫入資料庫
def data2sql_records():
    with open('data/explosiveapi2.json', 'r') as f:
        df = json.load(f)['records']
        for i, row in enumerate(df):
            if np.mod(i, 100) == 0:
                print(i)
            insert(row, 'explosive_records')


# 易爆物化學物質表
def data2sql_chemilist():
    with open('data/explosiveapi2.json', 'r') as f:
        df = json.load(f)['chemlist']
        for i, idf in enumerate(df):
            df[i]['chnname'] = df[i].pop('name')

        for i, row in enumerate(df):
            if np.mod(i, 100) == 0:
                print(i)
            insert(row, 'explosive_chemilist')


# 將原始資料寫入資料庫
def data2sql_rawdata():
    def colName():
        return [
            'DeclareTime',
            'DeptID',
            'CASNo',
            'ChemicalChnName',
            'ChemicalEngName',
            'SourceDept',
            'ResponsibleName',
            'ResponsibleTel',
            'ResponsiblePhone',
            'EmergencyName',
            'EmergencyTel',
            'EmergencyPhone',
            'ComFacBizName',
            'BusinessAdminNo',
            'FactoryRegNo',
            'ComFacBizAddress',
            'PlaceType',
            'RegionType',
            'RegionName',
            'ComFacBizTWD97X',
            'ComFacBizTWD97Y',
            'DeclareDate',
            'ImportQuantity',
            'ProductionQuantity',
            'ProductionTWD97X',
            'ProductionTWD97Y',
            'UseageQuantity',
            'UseageTWD97X',
            'UseageTWD97Y',
            'StorageQuantity',
            'StorageTWD97X',
            'StorageTWD97Y',
        ]

    dftmp = []
    for i in [1, 4, 7, 10]:
        tmp = pd.read_excel(
            "/Volumes/GoogleDrive-114782082393599805732/我的雲端硬碟/Project_Frontend/A1_explosive/2022/dataProc/files/整併報表_2021年度整理檔.xlsx",
            sheet_name=f"整併報表{i:02d}",
            header=[0, 1]
        )
        tmp = tmp[tmp.isna().sum(axis=1) < 39]
        dftmp.append(tmp)
    df = pd.concat(dftmp)
    df_drop = [i for i in df.columns if 'combine' in i[1]]
    df = df.drop(df_drop, axis=1).iloc[:, :32]
    df.columns = colName()
    df.DeclareTime = df.DeclareTime.astype(int)
    df = df.drop('DeclareDate', axis=1)
    for col in df.columns:
        df[col] = df[col].astype(str)
    df = df.to_dict(orient='records')

    for i, row in enumerate(df):
        if np.mod(i, 100) == 0:
            print(i)
        insert(row, 'explosive_rawdata')


def write_tojson(data, name):
    with open(f'src/info/{name}.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def chemMapping2testdb():
    sql = '''SELECT * FROM [ChemiPrimary].[dbo].[ChemiMatchMapping]'''
    df = pd.read_sql(sql, con=connSQL('db_chemtest_ssh'))
    df.to_sql(
        'ChemiMatchMapping',
        con=connSQL('dbtest'),
        index=False,
        if_exists='append',
        dtype={
            'MatchNo': sqlalchemy.types.INT,
            'CASNoMatch': sqlalchemy.types.NVARCHAR,
            'ChemiChnNameMatch': sqlalchemy.types.NVARCHAR,
            'ChemiEngNameMatch': sqlalchemy.types.NVARCHAR,
            'ChemiChnAliases': sqlalchemy.types.NVARCHAR,
            'ChemiEngAliases': sqlalchemy.types.NVARCHAR,
            'CreateDate': sqlalchemy.types.DATETIME,
            'ModifyDate': sqlalchemy.types.DATETIME,
        }
    )


def save2jsonserver():
    con = connSQL('dbtest')
    chemilist = pd.read_sql('select * from dbo.explosive_chemilist', con=con)
    data_all = pd.read_sql('select * from dbo.explosive_records_all', con=con)
    data_fac = pd.read_sql('select * from dbo.explosive_records_fac', con=con)
    data_city = pd.read_sql(
        'select * from dbo.explosive_records_city', con=con)
    chemilist = chemilist.replace('', np.nan).replace(np.nan, None)
    data_all = data_all.replace('', np.nan).replace(np.nan, None)
    data_fac = data_fac.replace('', np.nan).replace(np.nan, None)
    data_city = data_city.replace('', np.nan).replace(np.nan, None)

    with open('jsonapi/explosive.json', 'w') as f:
        json.dump({
            'chemilist': chemilist.to_dict(orient='records'),
            'records_all': data_all.to_dict(orient='records'),
            'records_city': data_city.to_dict(orient='records'),
            'records_fac': data_fac.to_dict(orient='records'),
        }, f, ensure_ascii=False, indent=2)

# 以上為資料準備
# ------------------------------------------------------------
# 以下為易爆物資料整理至寫入資料庫
# 讀取指引表


def getChemMap():
    sql = 'SELECT * FROM ChemiMatchMapping'
    cols = ['MatchNo', 'CASNoMatch', 'ChemiChnNameMatch', 'ChemiEngNameMatch',
            'ChemiChnAliases', 'ChemiEngAliases']
    chemMap = pd.read_sql(sql, con=connSQL('db_chemtest_ssh'))[cols]
    chemMap_e2n = chemMap.set_index('ChemiEngNameMatch')[
        'CASNoMatch']  # .str.lower()
    chemMap_e2n.index = chemMap_e2n.index.str.lower()
    chemMap_e2n = chemMap_e2n.to_dict()
    chemMap_n2e = chemMap.set_index('CASNoMatch')[
        'ChemiEngNameMatch']  # .str.lower()
    chemMap_n2e = chemMap_n2e.to_dict()
    return {'e2n': chemMap_e2n, 'n2e': chemMap_n2e}


def getChemMapExp():
    pth = pathlib.Path(os.path.abspath('.'))
    with open(pth/'src/info/explosive_nameMap.json') as f:
        namemap = json.load(f)
    return namemap


def groupBy(data, cols=[('ComFacBizName', ''), ('ComFacBizAddress', ''), ('import_info', 'X'), ('import_info', 'Y')]):
    data = copy.deepcopy(data)
    # data = copy.deepcopy(p.df2)
    col_merge = ['-'.join(i) if i[1] != '' else i[0] for i in data.columns]
    col_by = ['-'.join(i) if i[1] != '' else i[0] for i in cols]
    data.columns = col_merge
    s = data[col_by].assign(group='', status=0).sort_values(by='ComFacBizName')
    sn = copy.deepcopy(s)
    groupind = 0
    for j, [i, row] in enumerate(s.iterrows()):
        if sn.loc[i, 'group'] != '':
            continue
        if np.mod(groupind, 500) == 0:
            print(groupind)

        s1 = s.iloc[:, :2]
        s2 = pd.concat(
            [row.iloc[:2].to_frame().T] * len(s)).reset_index(drop=True)
        s2.index = s1.index
        ind = (s1 == s2).sum(axis=1)
        ind2 = sn[ind > 0].index
        sn.loc[ind2, 'group'] = groupind
        sn.loc[ind2, 'status'] = ind
        groupind += 1

    grp2name = sn[['group', 'ComFacBizName']].groupby(['group']).agg(
        lambda i: i.iloc[0])
    sn['ComFacBizName_m'] = sn['group'].map(grp2name.ComFacBizName)
    data2 = pd.concat([data, sn['ComFacBizName_m']], axis=1)
    return data2


def wide2long(data):
    data2 = {}
    for operation in ['import', 'produce', 'usage', 'storage']:
        cols1 = ['time', 'deptid', 'casno', 'PlaceType',
                 'RegionType', 'ComFacBizName', 'ComFacBizName_m']
        cols2 = [f'{operation}_info-{i}' for i in ['Quantity', 'X', 'Y']]
        cols = cols1 + cols2
        data2[operation] = data[cols]

    # 將運作行為中，同期別、同化學物質、同來源、同廠商、同座標的資料加總
    data3 = copy.deepcopy(data2)
    for key in data2.keys():
        colname = f'{key}_info-Quantity'
        item = data2[key].reset_index()

        item = item.astype({colname: float, 'index': str})
        item = item[item[colname] > 0]
        aggfun = {
            colname: 'sum',
            'PlaceType': lambda i: ','.join(i),
            'RegionType': lambda i: ','.join(i),
            'index': lambda i: ','.join(i),
            'count': 'count'
        }
        item_1 = (
            item[item[f'{key}_info-X'] != '-']
            .assign(count=0)
            .groupby([
                'ComFacBizName_m', 'casno', 'time', 'deptid', f'{key}_info-X',
                f'{key}_info-Y'])
            .agg(aggfun)
        )

        item_2 = (
            item[item[f'{key}_info-X'] == '-']
            .set_index([
                'ComFacBizName_m', 'casno', 'time', 'deptid', f'{key}_info-X',
                f'{key}_info-Y'])
        )

        data3[key] = (
            pd.concat([item_1, item_2])
            .sort_index()
            .rename({f'{key}_info-Quantity': 'Quantity'}, axis=1)
            .rename_axis(
                index=lambda i: i.replace(f'{key}_info-', ''))
        )
    data4 = pd.concat(data3).rename_axis(
        index={None: 'operation'}).reset_index()
    data4['name'] = data4['casno'].map(getChemMapExp())
    return data4


def locateCounty(data):
    data.loc[data[data.X == '-'].index, 'X'] = None
    data.loc[data[data.Y == '-'].index, 'Y'] = None
    # 二度分帶 to WGS
    data2 = gpd.GeoDataFrame(
        data, geometry=gpd.points_from_xy(data['X'], data['Y'], crs='epsg:3826'))
    data2 = data2.to_crs('epsg:4326')
    data2['lon'] = data2.geometry.apply(
        lambda i: i.x if not i.is_empty else '')
    data2['lat'] = data2.geometry.apply(
        lambda i: i.y if not i.is_empty else '')

    # 行政區定位
    taiwan = gpd.read_file('src/info/county.json')
    taiwan = taiwan.set_index("COUNTYNAME")['geometry']
    geometry = data2[['geometry']]
    pnts = geometry.assign(**{key: geometry.within(geom)
                              for key, geom in taiwan.items()})
    q = pnts.iloc[:, 1:].replace(
        False, np.nan).stack().reset_index().iloc[:, :2].set_axis(['index', 'city'], axis=1).set_index('index')
    data3 = data2.merge(q, left_index=True, right_index=True, how='left')
    data3.city = data3.city.fillna('')
    data4 = pd.DataFrame(data3.drop(columns=['geometry']))
    return data3


def statisticByCity(data):
    data2 = data.groupby(['time', 'operation', 'name',  'city'])[
        'Quantity'].sum().reset_index()
    return data2


def statisticByFac(data):
    data2 = data.groupby([
        "time", "operation", "name", "lon", "lat", "ComFacBizName_m", 'deptid']
    ).agg({'Quantity': 'sum'}).reset_index()
    return data2


def handleProcRecord(method, nlen=None):
    import datetime
    now = datetime.datetime.now()
    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    # db = client["explosive"]
    db = connMongo(machineName)
    col = db['status']
    if method == 'save':
        if 'status' not in db.list_collection_names():
            col.insert_one(
                {"name": "history", "count": nlen, "updatetime": now})
        else:
            col.update_one({"name": "history"}, {
                "$set": {"count": nlen, "updatetime": now}})
    elif method == 'load':
        nlen = col.find_one({"name": 'history'})['count']
        return nlen


class proc_explosive():
    def __init__(self, machineName, method='overwrite'):
        self.method = method
        self._getChemMap()
        self._getExplosiveData(machineName)
        self.procChemName(copy.deepcopy(self.df.chem))
        # self.df3 = groupBy(self.df2)
        # self.df4 = wide2long(self.df3)
        # self.df5 = locateCounty(self.df4)

    def _getChemMap(self):
        self.chemMapAll = getChemMap()
        self.chemMapExplosive = getChemMapExp()

    def _getExplosiveData(self, machineName):
        sql = 'SELECT * FROM ChemiPrimary.dbo.ExplosiveMergeData'
        if self.method == 'append':
            sql += ' where isProc=0'
        df = pd.read_sql(sql, con=connSQL(machineName))

        df = df.drop([
            'FCOUNTY', 'FTOWN', 'FCOUNTY_TOWN', 'CountyTownship', 'UpdateDate',
            'IsMerge', 'ProductionZipCode', 'UseageZipCode', 'StorageZipCode'], axis=1)

        pth = pathlib.Path(os.path.abspath('.'))
        with open(pth/'src/info/explosive_columns.json') as f:
            cols = json.load(f)

        df = df[cols['used']]
        df.columns = pd.MultiIndex.from_tuples(cols['nameMap'])
        self.df = df

    def procChemName(self, chem):
        # 整理casno，將不在列表內的物質移除
        cas2nameAlle2n = self.chemMapAll['e2n']
        cas2nameExp = self.chemMapExplosive
        chem.cname = chem.cname.map(cas2nameExp).map(cas2nameExp)
        chem.casno = chem.casno.map(cas2nameExp).map(cas2nameExp)
        chem.ename = chem.ename.str.lower().map(
            cas2nameAlle2n).map(cas2nameExp)  # .map(cas2nameExp)
        chem['cn2cas'] = chem.cname.map(cas2nameExp)
        chem['en2cas'] = chem.ename.str.lower().map(cas2nameExp)
        chem['cas2cn'] = chem.casno.map(cas2nameExp)
        chem = chem.fillna('')

        # 將沒有casno的物質以中英文名取代
        chem.loc[chem[chem.casno == ''].index,
                 'casno'] = chem.loc[chem[chem.casno == ''].index, 'cn2cas']
        chem.loc[chem[chem.casno == ''].index,
                 'casno'] = chem.loc[chem[chem.casno == ''].index, 'en2cas']
        chem = chem[['casno']]
        chem.columns = pd.MultiIndex.from_tuples([('casno', '')])
        self.chem = chem

        self.df = self.df.drop('chem', axis=1).merge(
            chem, left_index=True, right_index=True)
        self.df2 = self.df.drop(self.df[self.df.casno == ''].index)


def saveRecords(data, colname, method):
    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    # db = client["explosive"]
    db = connMongo(machineName)
    col = db[colname]
    if method == 'overwrite':
        col.delete_many({})
    col.insert_many(data)


if __name__ == '__main__':
    method = 'overwrite'
    machineName = 'db_chemtest'
    p = proc_explosive(machineName, method=method)
    df3 = groupBy(p.df2)  # 以廠商名稱、地址、座標分組
    df4 = wide2long(df3)  # 資料統整
    df5 = locateCounty(df4)  # 座標轉換與定位
    df5 = pd.DataFrame(df5.drop(columns=['geometry']))
    df5.time = df5.time.astype(int)
    df6 = statisticByCity(df5)
    df7 = statisticByFac(df5)
    df5_save = df5.fillna('-').to_dict(orient='records')
    df6_save = df6.fillna('-').to_dict(orient='records')
    df7_save = df7.fillna('-').to_dict(orient='records')

    saveRecords(df5_save, colname='records_all', method=method)
    saveRecords(df6_save, colname='records_city', method=method)
    saveRecords(df6_save, colname='records_fac', method=method)
