import asyncio
import json
from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from src.mongo_tools import get_conn as connMongo
# import pymongo
import socket

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.unicode.ambiguous_as_wide', True)

app = FastAPI()

origins = [
    # "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    # ComFacBizName_m: str | None = None
    # casno: str | None = None
    # name: str | None = None
    # time: str | None = None
    # deptid: str | None = None
    city: str | None = None


@app.get("/")
def test():
    return 'hello world'


@app.get("/explosiveapi/{kind}")
async def explosive(
        kind: str,
        city: str = None,
        ComFacBizName_m: str = None,
        name: str = None,
        casno: str = None,
        label: str = None,
        operation: str = None,
        time: int = None,
        time_ge: int = None,
        time_le: int = None,
):
    # async def explosive(kind: str):
    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    # db = client["explosive"]
    machineName = socket.gethostname()
    db = connMongo(machineName)
    if db:
        col = db[kind]
        query = {}
        # if kind == 'records_all':
        if ComFacBizName_m is not None:
            query = query | {'ComFacBizName_m': {'$regex': ComFacBizName_m}}
        if casno is not None:
            query = query | {'casno': {'$regex': casno}}
        if name is not None:
            query = query | {'name': {'$regex': name}}
        if label is not None:
            query = query | {'label': {'$regex': label}}
        if operation is not None:
            query = query | {'operation': {'$regex': operation}}
        if city is not None:
            query = query | {'city': {'$regex': city}}
        if time is not None:
            query = query | {'time': time}
        if time_ge is not None:
            query = query | {'time': {'$gte': time}}
        if time_le is not None:
            query = query | {'time': {'$lte': time}}
        data = col.find(query, {'_id': False})
        res = list(data)
        # elif kind == 'chemilist':
        #     data = col.find({'label': {'$regex': name}})
        #     return list(data)
        return res
    else:
        return 'server error'
