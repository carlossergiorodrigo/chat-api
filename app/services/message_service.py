from ..model.message import Message
from .. import db


class MessageService():

    def save_message(message):
        db.session.add(message)
        db.session.commit()

        return message


    def get_messages_from_user(recipent, starting_message, limit=100):
        return Message.query.filter(Message.id >= starting_message, Message.recipient == recipent).order_by(Message.id).limit(limit)
