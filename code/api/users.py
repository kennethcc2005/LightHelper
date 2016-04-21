from . import api
from nested_blueprint import NestedBlueprint

users = NestedBlueprint(api, 'users')

@users.route('/', methods=['GET'])
def test():
    return 'success'