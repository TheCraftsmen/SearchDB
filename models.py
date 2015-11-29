from app import db
import datetime


class HostPing(db.Model):

    tablename__ = "hostPing"

    table_id = db.Column(db.Integer, primary_key=True)
    hostName = db.Column(db.String, nullable=True)
    fantasyName = db.Column(db.String, nullable=True)
    connectStatus = db.Column(db.String, nullable=True)
    connectTime = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, hostName, connectStatus, fantasyName):
        self.hostName = hostName
        self.connectStatus = connectStatus
        self.fantasyName = fantasyName

    def __repr__(self):
        pass