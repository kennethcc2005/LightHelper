from flask import Blueprint
from ..controllers.util import create_user

users = Blueprint('users', __name__, url_prefix='api/users')

@users.route('/register', methods=['POST'])
def register():
    print request.methods
    data = json.loads(request.get_data())
    data['email'] = data['email'].lower()
    user = create_user(data['email'], data.get('username'), data.get('first_name'), data.get('last_name'),
                data.get('password'))
    return user

@users.route('/test', methods=['GET'])
def test():
    return 'success'