from datetime import timedelta
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from os import getenv
import redis

ACCESS_EXPIRES = timedelta(hours=1)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = getenv('SECRET_KEY')

jwt = JWTManager(app)

jwt_redis_blocklist = redis.StrictRedis(
    host="localhost", port=8080, db=0, decode_responses=True
)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None

@app.route('/login', methods=['POST'])
def login():
    payload = request.json
    user = {
        'id': 2,
        'username': 'ziddd',
        'password': 'z'
    }
    if payload['username'] == user['username'] and payload['password'] == user['password']:
        return jsonify({
            'status': 200,
            'data': {
                'access_token': create_access_token(identity=user)
            },
            'message': 'success'
        }), 200
    else:
        return jsonify({
            'status': 400,
            'data': 'periksa username dan password anda',
            'message': 'error'
        }), 400

@app.route('/user')
@jwt_required()
def user():

    return jsonify({
        'status': 200,
        'data': get_jwt_identity(),
        'message': 'success'
    })

@app.route('/')
def index():
    return jsonify({
        'status': 200,
        'data': '',
        'message': 'success'
    })