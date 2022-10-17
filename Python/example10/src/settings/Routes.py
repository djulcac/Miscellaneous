import datetime
import json

from flask import Blueprint, render_template, session, abort, request, g

from ..handlers import UserHandler
from .. import utils

url_prefix = '/api/0.1'
app_routes = Blueprint('api0_1',__name__,url_prefix=url_prefix)

@app_routes.route('/',methods=['GET'])
@app_routes.route('',methods=['GET'])
def index():
    # print(datetime.datetime.now(),__name__,url_prefix,'index',g.vg['log'],request.method)
    utils.Log.log(__name__,request.method)
    return {"hello":"world"}

@app_routes.route('/users',methods=['POST'])
def usersPOST():
    # print(datetime.datetime.now(),__name__,url_prefix,'signup',g.vg['log'],request.method)
    utils.Log.log(__name__,request.method)
    return UserHandler.create()

@app_routes.route('/users',methods=['GET'])
def usersGET():
    utils.Log.log(__name__,request.method)
    return UserHandler.get_all()

@app_routes.route('/users/<int:ID>',methods=['GET'])
def users_idGET(ID):
    utils.Log.log(__name__,request.method)
    return UserHandler.get_one(ID)

@app_routes.route('/users/<int:ID>',methods=['DELETE'])
def users_idDELETE(ID):
    utils.Log.log(__name__,request.method)
    return UserHandler.delete(ID)

@app_routes.route('/users/<int:ID>',methods=['PUT'])
def users_idPUT(ID):
    utils.Log.log(__name__,request.method)
    return UserHandler.update(ID)

# https://www.moesif.com/blog/technical/api-design/REST-API-Design-Best-Practices-for-Sub-and-Nested-Resources/
