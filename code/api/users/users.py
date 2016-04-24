import json
from . import users
from sqlalchemy.exc import OperationalError
from flask import Blueprint, Response, g, request, jsonify
from ..controllers.util import create_user

@users.route('/register', methods=['POST'])
def register():
    data = request.get_data()
    user = create_user(data['email'], data.get('username'), data.get('first_name'), data.get('last_name'),
                data.get('password'))
    return user

@users.route('/test', methods=['GET'])
def test():
    return 'success'