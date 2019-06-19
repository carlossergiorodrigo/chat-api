from flask import request, make_response, jsonify
from flask import current_app as app
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from .model.user import UserSchema
from .model.message import MessageSchema
from .helpers.hash_helper import HashHelper
from .services.user_service import UserService
from .services.message_service import MessageService
from .services.authorization_service import AuthorizationService


@app.route('/check', methods=['GET', 'POST'])
def check():
    return jsonify(health="ok")

@app.route('/users', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        try:
            request_data = request.get_json(force=True)
            user_schema = UserSchema(strict=True).load(request_data)
        except ValidationError as err:
            return jsonify(err.messages), 500
        
        user = UserService.save_user(user_schema.data)
        return jsonify(id=user.id)
    else:
        return 'method not implemented', 501

@app.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json(force=True)
        user_schema = UserSchema(strict=True).load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 500

    user = UserService.get_user_by_username(user_schema.data.username)
    
    if not user:
        return 'user not found', 401
    
    if HashHelper.verify_hash(user_schema.data.password, user.password):
        token = AuthorizationService.get_token(user.id)
        return jsonify(id=user.id,
                       token=token), 200
    else:
        return 'invalid password', 401

@app.route('/messages', methods=['POST'])
@jwt_required
def send_message():
    try:
        request_data = request.get_json(force=True)
        message = MessageSchema(strict=True).load(request_data).data
    except ValidationError as err:
        return jsonify(err.messages), 500

    current_user_id = get_jwt_identity()

    if current_user_id is not message.sender:
        return 'unauthorized message', 401

    MessageService.save_message(message)

    return jsonify(id=message.id,
                   timestamp=message.creation_date)

@app.route('/getMessages')
@jwt_required
def get_messages():
    recipent = request.args.get('recipent')
    start = request.args.get('start')
    limit = request.args.get('limit')

    if recipent is None:
        return 'recipent is a required parameter', 400

    if start is None:
        return 'start is a required parameter', 400

    if limit is not None:
        messages = MessageService.get_messages_from_user(recipent, start, limit)
    else:
        messages = MessageService.get_messages_from_user(recipent, start)
    
    schema = MessageSchema(many=True)
    result = schema.dump(messages)

    return jsonify(messages=result)
