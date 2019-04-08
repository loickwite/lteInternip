from flask import request
from flask_restful import Resource

rsrp = []
rsrq = []
rssi = []
sinr = []
pci = []
bler = []

class Rsrp(Resource):
    data = request.json['rsrp']
    rsrp.append(data)
    return {'status':'success'}

class Rsrq(Resource):
    data = request.json['rsrq'] 
    rsrq.append(data)
    return {'status':'success'}

class Rssi(Resource):
    data = request.json['rssi']
    rssi.append(data)
    return {'status':'success'}

class Sinr(Resource):
    data = request.json['sinr']
    sinr.append(data)
    return {'status':'success'}

class Pci(Resource):
    data = request.json['pci']
    pci.append(data)
    return {'status':'success'}

class Bler(Resource):
    data = request.json['bler']
    bler.append(data)
    return {'status':'success'}
