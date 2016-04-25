import os
import hmac
import json
from flask import current_app
from ..models import models
from passlib.hash import sha256_crypt
from app import db

def _encrypt_password(password):
    salt = current_app.config.get('LOGIN_SECRET_KEY', '')
    encoded = sha256_crypt.encrypt(salt)
    return encoded

def create_user(email, username, first_name, last_name, password):
    user_data = {'email': email,
                 'username': username,
                 'first_name': first_name,
                 'last_name': last_name,
                 'password': _encrypt_password(str(password))}
    user = models.User(**user_data)
    db.session.add(user)
    db.session.commit()

    return user