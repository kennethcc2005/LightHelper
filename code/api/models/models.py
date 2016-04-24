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
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    created_ts = db.Column(
        TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_update = db.Column(
        TIMESTAMP, server_default=text('now()'), nullable=False)

    def __init__(self, **user_data):
        self.id = uuid.uuid4().hex
        self.email = user_data["email"]
        self.username = user_data["username"]
        self.password = user_data["password"]
        self.first_name = user_data["first_name"]
        self.last_name = user_data["last_name"]
        self.role = 'volunteer'
        self.updated_ts = datetime.datetime.now()
        
    def __repr__(self):
        return '<User %r>' % self.email

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __unicode__(self):
        return self.email


if __name__ == '__main__':
    manager.run()