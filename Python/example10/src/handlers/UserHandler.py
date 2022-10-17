import datetime

from flask import request,g

from ..services import UsersService as Service
from .. import utils
from ..settings import Settings

_model = 'users'

def create():
    "bien bien okok"
    try:
        utils.Log.log(__name__,'start')
        data = request.get_json()
        if data == None:
            return utils.ErrorResponse.Error(message='Empty JSON content.',code=400)
        e = validate_create(data)
        if len(e) > 0:
            return utils.ErrorResponse.Error(message=e[0],code=400)
        
        r = Service.create(data)
        if r['error']:
            if r['type'] == 'unique':
                return utils.ErrorResponse.Error(
                    message=f'The {r["column"]} already exists.',code=409,
                    subcode=4090, subvalue=r['column']
                )
            if r['type'] == 'validate':
                return utils.ErrorResponse.Error(
                    message=r['message'],code=400,
                )
            raise Exception('Error(625.6850329999246)::')
        data['id'] = r['id']
        _code = 201
        return {"status":"success","code":_code,"data":data},_code
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        return utils.ErrorResponse.Error(code=500)

def validate_create(data):
    e = []
    if not 'email' in data:
        e.append('Value "email" is required')
    else:
        if len(data['email']) <= 3:
            e.append('Value "email" must not be empty')
    if not 'name' in data:
        e.append('Value "name" is required')
    else:
        if len(data['name'])<1:
            e.append('Value "name" must not be empty')
    return e

def get_filter(data):
    columns = ['id','name','lastname','email','phone','createdAt','updatedAt']
    _filter = []
    for key in data:
        if not key in columns:
            _filter.append(key)
    for key in _filter:
        del data[key]
    return data

def get_all():
    try:
        utils.Log.log(__name__,'start')
        _limit = request.args.get('limit')
        _offset = request.args.get('offset')
        _limit_system = Settings.config['limits']['default']
        if _model in Settings.config['limits']:
            _limit_system = Settings.config['limits'][_model]
        
        if _limit == None:
            _limit = _limit_system
        else:
            _limit = int(_limit)
            if _limit > _limit_system:
                _limit = _limit_system
        if _offset == None:
            _offset = 0
        else:
            _offset = int(_offset)
        
        r = Service.get_all(_offset,_limit)
        for x in r['data']:
            if x['createdAt'] : x['createdAt'] = x['createdAt'].isoformat()
            if x['updatedAt'] : x['updatedAt'] = x['updatedAt'].isoformat()
        ans = []
        for x in r['data']:
            ans.append(get_filter(x))
        return {
            "monty":"python",
            "data":ans,
            "count":r['count'],
            "limit":r['limit'],"offset":r['offset'],
        }
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        return utils.ErrorResponse.Error(code=500)

def get_one(ID):
    try:
        utils.Log.log(__name__,'start')
        
        r = Service.get_one(ID)
        if r['count'] == 0:
            return utils.ErrorResponse.Error(message=f'Not found id={ID}',code=404)
        x = r['data']
        if x['createdAt'] : x['createdAt'] = x['createdAt'].isoformat()
        if x['updatedAt'] : x['updatedAt'] = x['updatedAt'].isoformat()
        return {
            "monty":"python",
            "data":get_filter(r['data']),
        }
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        return utils.ErrorResponse.Error(code=500)

def delete(ID):
    try:
        utils.Log.log(__name__,'start')
        r = Service.delete(ID)
        return '',r['code']
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        return utils.ErrorResponse.Error(code=500)

def update(ID):
    try:
        utils.Log.log(__name__,'start')
        data = request.get_json()
        if data == None:
            return utils.ErrorResponse.Error(message='Empty JSON content.',code=400)
        e = validate_update(data)
        if len(e) > 0:
            return utils.ErrorResponse.Error(message=e[0],code=400)
        
        r = Service.update(ID,data)
        if r['error']:
            if r['type'] == 'unique':
                return utils.ErrorResponse.Error(
                    message=f'The {r["column"]} already exists.',code=409,
                    subcode=4090, subvalue=r['column']
                )
            if r['type'] == 'validate':
                return utils.ErrorResponse.Error(
                    message=r['message'],code=400,
                )
            if r['type'] == '404':
                return utils.ErrorResponse.Error(
                    code=404,
                )
            raise Exception('Error(862.5825567508889)::')
        
        _code = 201
        return {"status":"success","code":_code},_code
    except Exception as errors:
        utils.ErrorManage.printErrors(errors)
        return utils.ErrorResponse.Error(code=500)

def validate_update(data):
    'formato de email, o formatos'
    e = []
    # not null
    if 'email' in data:
        if data['email'] == None:
            e.append('Value email is required')
    return e
