import os
import hmac
import json
import base64
import urllib2
import hashlib
from flask import current_app
from ..models.models import User

def _encrypt_password(password):

    def encode_string(string):

        if isinstance(string, unicode):
            string = string.encode('utf-8')
        return string

    salt = current_app.config.get('LOGIN_SECRET_KEY', '')
    signed = hmac.new(encode_string(salt), encode_string(password), hashlib.sha512)
    pwd_context = CryptContext(schemes=['pbkdf2_sha512'], default='pdkdf2_sha512')
    return pwd_context.encrypt(base64.b64encode(signed.digest()).decode('ascii'))

def create_user(email, username, first_name, last_name, password):
    user_data = {'email': email,
                 'username': username,
                 'first_name': first_name,
                 'last_name': last_name,
                 'password': _encrypt_password(password)}
    user = User(**user_data)
    db.session.add(user)
    db.session.flush()

    return user
