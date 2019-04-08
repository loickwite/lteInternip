from flask import request
from flask_restful import Resource
from model import db, KPI_2G
from modelSer import KPI_2GSchema

kpi_2g_schema = KPI_2GSchema()

rxLevel = []
rxQual = []

class RxLevel(Resource):
    data = request.json['rxlevel']
    rxLevel.append(data)
    return {'status':'success'}

class RxQual(Resource):
    data = request.json['rxqual']
    rxLevel.append(data)
    return {'status':'success'}