import datetime as dt

from .. import db
from marshmallow import fields, Schema, post_load


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer,
                   primary_key=True)
    sender = db.Column(db.Integer,
                       index=True,
                       unique=False,
                       nullable=False)
    recipient = db.Column(db.Integer,
                          index=True,
                          unique=False,
                          nullable=False)
    # Only to get metrics about message types
    type = db.Column(db.String(8),
                     unique=False,
                     nullable=False,
                     index=True)
    content = db.Column(db.JSON,
                        unique=False,
                        nullable=False,
                        index=False)
    creation_date = db.Column(db.DateTime,
                              unique=False,
                              index=False,
                              nullable=False)
    def __init__(self, sender, recipient, type, content):
        self.sender = sender
        self.recipient = recipient
        self.type = type
        self.content = content
        self.creation_date = dt.datetime.now()

    def __repr__(self):
        return '<Message(sender={self.sender!r})>'.format(self=self)

class MessageSchema(Schema):
    id = fields.Integer()
    sender = fields.Integer(required=True,
                            error_messages={'required': 'sender is required.'})
    recipient = fields.Integer(required=True,
                               error_messages={'required': 'recipient is required.'})
    content = fields.Dict()
    creation_date = fields.Date()

    @post_load
    def make_message(self, data):
        content = data['content']
        return Message(data['sender'], data['recipient'], content['type'], content)

