"""Authorization Service"""
from flask_jwt_extended import create_access_token

class AuthorizationService():

    @staticmethod
    def get_token(username):
        """Return a token using username as identifier"""
        return create_access_token(identity=username)
