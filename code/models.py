import datetime
import uuid
from sqlalchemy.sql.expression import text, false
from sqlalchemy.types import TIMESTAMP, Numeric
from sqlalchemy.dialects.postgresql import ENUM
import sqlalchemy.ext.mutable
from app import db, manager

class User(db.Model):
    __tablename__ = 'givelight_user'

    id = db.Column(db.String(1024), primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(128), nullable=False, unique=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    userattribute = db.relationship('UserAttribute', uselist=False)
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
        return "<User(name='%s %s')>" % (self.first_name, self.last_name)

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

class UserAttribute(db.Model):
    __tablename__ = 'givelight_user_attribute'

    id = db.Column(db.String(1024), primary_key=True)
    user_id = db.Column(
        db.String(1024), db.ForeignKey('givelight_user.id'), nullable=False, unique=True)
    address_line1 = db.Column(db.String(64), nullable=True)
    address_line2 = db.Column(db.String(64), nullable=True)
    city = db.Column(db.String(30), nullable=True)
    state = db.Column(db.String(30), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)
    country = db.Column(db.String(40), nullable=True)
    created_ts = db.Column(
         TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_ts = db.Column(
         TIMESTAMP, default=db.func.now(), onupdate=db.func.now(), nullable=False)


    def __init__(self, user):
        self.id = uuid.uuid4().hex
        self.user_id = user

class Event(db.Model):
    __tablename__ = 'givelight_event'

    id = db.Column(db.String(1024), primary_key=True)
    event_name = db.Column(db.String(1024), nullable=False)
    event_time = db.Column(db.DateTime(timezone=False), nullable=True)
    location = db.Column(db.String(1024), nullable=False)
    # task = db.relationship('Task')
    created_ts = db.Column(
         TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_ts = db.Column(
         TIMESTAMP, default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def __init__(self):
        self.id = uuid.uuid4().hex

class Task(db.Model):
    __tablename__ = 'givelight_task'

    id = db.Column(db.String(1024), primary_key=True)
    description = db.Column(db.String(1024), nullable=False)
    deadline = db.Column(db.DateTime(timezone=False), nullable=True)
    completed = db.Column(db.Boolean(), default=True, nullable=True)
    frequency = db.Column(ENUM('per_event', 'monthly', 'quarterly', 'annually'), server_default='per_event', nullable=True)
    progress_percentage = db.Column(db.Integer, server_default='0', nullable=False)
    urgency_level=db.Column(ENUM('1','2','3','4','5'), server_default='1', nullable=False)
    # event_id = db.Column(
        # db.String(1024), db.ForeignKey('givelight_event.id'), nullable=False)
    created_ts = db.Column(
         TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_ts = db.Column(
         TIMESTAMP, default=db.func.now(), onupdate=db.func.now(), nullable=False)


    def __init__(self):
        self.id = uuid.uuid4().hex


if __name__ == '__main__':
    manager.run()