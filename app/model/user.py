import datetime as dt

from .. import db
from ..helpers.hash_helper import HashHelper
from marshmallow import Schema, fields, post_load

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                           index=False,
                           unique=True,
                           nullable=False)
    password = db.Column(db.String(64),
                          index=False,
                          unique=False,
                          nullable=False)
    creation_date = db.Column(db.DateTime,
                              index=False,
                              unique=False,
                              nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.creation_date = dt.datetime.now()

    def __repr__(self):
        return '<User(name={self.username!r})>'.format(self=self)

class UserSchema(Schema):
    username = fields.String(required=True,
                             error_messages={'required': 'username is required.'})
    password = fields.String(required=True,
                             error_messages={'required': 'password is required.'})
    creation_date = fields.Date()

    @post_load
    def make_user(self, data):
        return User(data['username'], data['password'])
