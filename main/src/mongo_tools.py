import pymongo
from configparser import ConfigParser
from src.handleException import getError

config = ConfigParser()
config.read('src/conf.ini')


def get_conn(machineName):
    if machineName != 'EULSTCF':
        machineName = 'other'
    server = config[machineName]['mongo_server']
    try:
        print(f"mongodb://{server}:27017/")
        client = pymongo.MongoClient(
            f"mongodb://{server}:27017/", serverSelectionTimeoutMS=5)
        client.server_info()
        db = client["explosive"]
        print(2)
        return db
    except Exception as e:
        print('error')
        getError(e)
        return False
