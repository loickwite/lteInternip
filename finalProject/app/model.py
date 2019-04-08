from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Ssv(db.Model):
    __tablename__ = 'ssv'
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(250), nullable=False)
    antenna_type = db.Colum(db.Integer, nullable=False) #360, 180, 120
    operator = db.Column(db.String(250), nullable=False)
    town = db.Column(db.String(250), nullable=False)
    quarter = name = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Datetime, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    network = db.Column(db.String(250), nullable=False)
    kpi_2g = db.relationship('KPI_2G', backref=db.backref('ssv2', lazy='dynamic' ))
    kpi_3g = db.relationship('KPI_3G', backref=db.backref('ssv3', lazy='dynamic' ))
    kpi_4g = db.relationship('KPI_4G', backref=db.backref('ssv4', lazy='dynamic' ))

    def __init__(self, site_name, antenna_type, operator, town, quarter, date, longitude, latitude, network):
        self.site_name = site_name
        self.antenna_type = antenna_type 
        self.operator = operator
        self.town = town
        self.quarter = quarter
        self.date = date
        self.longitude = longitude
        self.latitude = latitude
        self.network = network
        self.kpi = returnKPI(network)
        
    def returnKPI(network):
        if network == "2G":
            return KPI_2G()
        if network == "3G":
            return KPI_3G()
        if network == "4G":
            return KPI_4G()


class Kpi():
    
    def __init__(self):
        self.cssr = 0
        self.cdr = 0
        self.ul = 0
        self.dl = 0
        self.hosr = 0
        self.reselect = 0

class KPI_2G(db.Model, Kpi):
    __tablename__ = 'kpi_2g'
    id = db.Column(db.Integer, primary_key=True)
    rxLevel = db.Column(db.Float, nullable=False)
    rxQual = db.Column(db.Float, nullable=False)

    cssr = db.Column(db.Float, nullable=False)
    cdr = db.Column(db.Float, nullable=False)
    hosr = db.Column(db.Float, nullable=False)
    ul = db.Column(db.Float, nullable=False)
    dl = db.Column(db.Float, nullable=False)
    reselect = db.Column(db.Float, nullable=False)

    ssv_id = db.Column(db.Integer, db.ForeignKey('ssv.id', ondelete='CASCADE'), nullable=False)


    def __init__(self):
        Kpi.__init__(self)
        self.rxLevel = 0
        self.rxQual = 0

class KPI_3G(db.Model, Kpi):
    id = db.Column(db.Integer, primary_key=True)
    rscp = db.Column(db.Float, nullable=False)
    sqi = db.Column(db.Float, nullable=False)
    ecno = db.Column(db.Float, nullable=False)
    
    cssr = db.Column(db.Float, nullable=False)
    cdr = db.Column(db.Float, nullable=False)
    hosr = db.Column(db.Float, nullable=False)
    ul = db.Column(db.Float, nullable=False)
    dl = db.Column(db.Float, nullable=False)
    reselect = db.Column(db.Float, nullable=False)

    ssv_id = db.Column(db.Integer, db.ForeignKey('ssv.id', ondelete='CASCADE'), nullable=False)


    def __init__(self):
        Kpi.__init__(self)
        self.rscp = 0
        self.sqi = 0   
        self.ecno = 0
        

class KPI_4G(db.Model, Kpi):
    id = db.Column(db.Integer, primary_key=True)
    rsrp = db.Column(db.Float, nullable=False)
    rsrq = db.Column(db.Float, nullable=False)
    rssi = db.Column(db.Float, nullable=False)
    sinr = db.Column(db.Float, nullable=False)
    pci = db.Column(db.Float, nullable=False)
    bler = db.Column(db.Float, nullable=False)
    
    cssr = db.Column(db.Float, nullable=False)
    cdr = db.Column(db.Float, nullable=False)
    hosr = db.Column(db.Float, nullable=False)
    ul = db.Column(db.Float, nullable=False)
    dl = db.Column(db.Float, nullable=False)
    reselect = db.Column(db.Float, nullable=False)

    ssv_id = db.Column(db.Integer, db.ForeignKey('ssv.id', ondelete='CASCADE'), nullable=False)

    def __init__(self):
        Kpi.__init__(self)
        self.rsrp = 0
        self.rsrq = 0   
        self.rssi = 0
        self.sinr = 0
        self.pci = 0   
        self.bler = 0
