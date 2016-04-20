import datetime
import uuid
from app import db, manager
from sqlalchemy.sql.expression import text, false
from sqlalchemy.types import TIMESTAMP, Numeric

class User(db.Model):
    __tablename__ = 'givelight_user'
    
    id = db.Column(db.String(1024), primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    role = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(1024), nullable=True)
    created_ts = db.Column(
        TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_update = db.Column(
        TIMESTAMP, server_default=text('now()'), nullable=False)

    def __init__(self, **user_data):
        self.id = uuid.uuid4().hex
        self.email = user_data["email"].lower()
        self.username = user_data["username"].lower()
        self.password = user_data["password"]
        self.first_name = user_data["first_name"]
        self.last_name = user_data["last_name"]
        self.updated_ts = datetime.datetime.now()

if __name__ == '__main__':
    manager.run()