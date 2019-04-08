from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow


ma = Marshmallow()

class SsvSchema(ma.Schema):
    id = ma.Integer()
    site_name = ma.String()
    antenna_type = ma.Integer()
    operator = ma.String()
    town = ma.String()
    quarter = ma.String()
    date = ma.Datetime()
    longitude = ma.Float()
    network = ma.String()

class KPI_2GSchema(ma.Schema):
    id = ma.Integer()
    rxLevel = ma.Float()
    rxQual = ma.Float()
    cssr = ma.Float()
    cdr = ma.Float()
    hosr = ma.Float()
    ul = ma.Float()
    dl = ma.Float()
    reselect = ma.Float()
    ssv_id = ma.Integer()

class KPI_3GSchema(ma.Schema):
    id = ma.Integer()
    rscp = ma.Float()
    sqi = ma.Float()
    ecno = ma.Float()
    cssr = ma.Float()
    cdr = ma.Float()
    hosr = ma.Float()
    ul = ma.Float()
    dl = ma.Float()
    reselect = ma.Float()
    ssv_id = ma.Integer()

class KPI_4GSchema(ma.Schema):
    id = ma.Integer()
    rsrp = ma.Float()
    rsrq = ma.Float()
    rssi = ma.Float()
    sinr = ma.Float()
    pci = ma.Float()
    bler = ma.Float()
    cssr = ma.Float()
    cdr = ma.Float()
    hosr = ma.Float()
    ul = ma.Float()
    dl = ma.Float()
    reselect = ma.Float()
    ssv_id = ma.Integer()
