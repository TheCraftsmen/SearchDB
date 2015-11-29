# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_restful import Resource, Api
from flask.ext.sqlalchemy import SQLAlchemy
import MySQLdb
import datetime

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
api = Api(app)

db = SQLAlchemy(app)
from models import *

todo = dict()


class TodoSimple(Resource):

    USER = 'user'
    PASSWD = 'passwd'

    def __init__(self):
        super(TodoSimple, self).__init__()

    def put(self):
        with open('./dbDocs/databases.txt', 'r') as hostfile:
            for row in hostfile:
                if row:
                    host, database = row.replace('\n', '').split(',')
                    self.dataConnection(str(host), str(database))
        return "Datos almacenados"

    def dataConnection(self, host, db):
        try:
            datab = MySQLdb.connect(host=host,
            user=self.USER, passwd=self.PASSWD, db=db)
            conexion = "hay conexion"
        except MySQLdb.OperationalError, e:
            conexion = "no hay conexion"
        self.dataCollector(host, conexion)

    def dataCollector(self, host, value):
        todo[host] = value
        db.session.query(HostPing).filter(HostPing.hostName == host).\
        update({'connectStatus': value, 'connectTime': datetime.datetime.now()})
        print datetime.datetime.now()
        db.session.commit()

    def get(self):
        listofhostping = list()
        connectQuery = HostPing.query.all()
        if connectQuery:
            for row in connectQuery:
                dicthost = dict(
                     hostname=row.hostName,
                     connectStatus=row.connectStatus,
                     connectTime=row.connectTime
                    )
                listofhostping.append(dicthost)
        return jsonify({'hostping': listofhostping})

api.add_resource(TodoSimple, '/_host_ping')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hostSave', methods=['GET', 'POST'])
def hostSave():
    if request.method == 'POST':
        print "hola"
        print request.form['hostName']
        if request.form['hostName'] and request.form['fantasyName']:
            hp = HostPing(hostName=request.form['hostName'],
            fantasyName=request.form['fantasyName'],
            connectStatus="no hay conexion")
            db.session.add(hp)
            db.session.commit()
        return redirect(url_for('hostSave'))
    return render_template('hostSave.html')


if __name__ == '__main__':
    app.run()