from flask import request
from flask_restful import Resource


 class Rates(Resource):
     cssr = request.json['cssr']
     cdr = request.json['cdr']
     hosr = request.json['hosr']
     ul = request.json['ul']
     dl = request.json['dl']
     reselect = request.json['reselect']