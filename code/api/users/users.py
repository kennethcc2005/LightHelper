import json
from . import users
from sqlalchemy.exc import OperationalError
from flask import Blueprint, Response, g, request, jsonify
from .util import create_user
import ast

@users.route('/register', methods=['POST'])
def register():
    data = request.get_data()
    data = ast.literal_eval(data)
    user = create_user(data['email'], data['username'], data['first_name'], data['last_name'],
                data['password'])
    return user

@users.route('/test', methods=['GET'])
def test():
    return 'success'