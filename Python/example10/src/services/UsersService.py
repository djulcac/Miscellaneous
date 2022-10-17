from datetime import datetime,timezone

import sqlalchemy

from .. import db
from ..models import Users as Model
from .. import utils

def create(data):
    try:
        utils.Log.log(__name__,'start')
        e = validate_create(data)
        if len(e) > 0:
            return {'error':True,'type':'validate','message':e[0]}
        return Model().insert(db,data)
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        raise Exception('Errors...')

def validate_create(data):
    e = []
    if not 'name' in data:
        e.append('Value name is required')
    if not 'email' in data:
        e.append('Value email is required')
    return e


def get_all(offset=0,limit=20):
    try:
        c,r = Model().get_all(db,offset=offset,limit=limit)
        data = []
        for x in r:
            data.append({
                "id" : x.id,
                "name" : x.name,
                "lastname" : x.lastname,
                "email" : x.email,
                "phone" : x.phone,
                "createdAt" : utils.Time.toutc(x.createdAt),
                "updatedAt" : utils.Time.toutc(x.updatedAt),
                "deleted" : x.deleted
            })
        return {
            "data":data,
            "count":c,
            "offset":offset,
            "limit":limit
        }
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        raise Exception('Errors...')

def get_one(ID):
    try:
        r = Model().get_one(db,ID)
        if r == None:
            return {"count":0,"data":{}}
        x = r
        data = {
            "id" : x.id,
            "name" : x.name,
            "lastname" : x.lastname,
            "email" : x.email,
            "phone" : x.phone,
            "createdAt" : utils.Time.toutc(x.createdAt),
            "updatedAt" : utils.Time.toutc(x.updatedAt),
            "deleted" : x.deleted
        }
        return {
            "count":1,
            "data":data,
        }
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        raise Exception('Errors...')

def delete(ID):
    try:
        r = Model().get_one(db,ID)
        if r == None:
            return {"error":True,"code":404}
        r = Model().delete(db,ID)
        return {"error":False,"code":204}
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        raise Exception('Errors...')

def update(ID,data):
    try:
        utils.Log.log(__name__,'start')
        r = get_one(ID)
        if r['count'] == 0:
            return {"error":True,"type":'404'}
        e = validate_update(data,r['data'])
        if len(e) > 0:
            return {'error':True,'type':'validate','message':e[0]}
        return Model().update(db,ID,data)
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        raise Exception('Errors...')

def validate_update(data,old):
    'validar unique y not null'
    e = []
    # not null
    for x in ['email','name']:
        if x in data:
            if data[x] == None:
                e.append(f'Value {x} is required')
    # same value
    # values = ['name','lastname','email','phone']
    # for x in values:
    #     if x in data and data[x] == old[x]:
    #         e.append(f'{x} has the same value')
    return e
