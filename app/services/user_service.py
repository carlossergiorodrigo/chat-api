from ..model.user import User
from ..helpers.hash_helper import HashHelper
from .. import db


class UserService():

    def save_user(user):
        user.password = HashHelper.generate_hash(user.password)
        db.session.add(user)
        db.session.commit()

        return user


    def get_user_by_username(username):
        return User.query.filter_by(username = username).first()
