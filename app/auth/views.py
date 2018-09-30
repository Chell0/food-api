# local import
from app.views import Users

users = [
    Users(1, 'admin', 'admin')
]

"""Find a user using the username"""
username_mapping = {us.username: us for us in users}

"""Find a user using the id"""
user_mapping = {us.id: us for us in users}

"""Authenticate a user"""


def auth(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


"""using the payload"""


def identity(payload):
    user_id = payload['identity']
    return user_mapping.get(user_id, None)
