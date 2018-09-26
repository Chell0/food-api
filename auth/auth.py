users = [
    {
        'id': 1,
        'username': 'admin',
        'password': 'admin'
    }
]

"""Find a user using the username"""
username_mapping = {'admin': {
        'id': 1,
        'username': 'admin',
        'password': 'admin'
   }
}

"""Find a user using the id"""

userid_mapping = { 1: {
        'id': 1,
        'username': 'admin',
        'password': 'admin'
    }
}


"""Authenticate a user"""
def auth(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

"""using the payload"""
def id(payload):
    user_id = payload['id']
    return userid_mapping.get(user_id, None)