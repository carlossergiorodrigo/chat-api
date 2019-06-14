from flask_jwt_extended import create_access_token

class AuthorizationService():

    @staticmethod
    def get_token(username):
        return create_access_token(identity=username)

