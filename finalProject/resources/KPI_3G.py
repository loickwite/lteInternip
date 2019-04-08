from flask import request
from flask_restful import Resource

rscp = []
sqi = []
ecno = []

class Rscp(Resource):
    data = request.json['sqi'])
    rscp.append(data)
    return {'status':'success'}

class Sqi(Resource):
    data = request.json['sqi']
    sqi.append(data)
    return {'status':'success'}

class Ecno(Resource):
    data = request.json['ecno']
    ecno.append(data)
    return {'status':'success'}