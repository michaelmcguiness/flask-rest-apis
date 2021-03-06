from werkzeug.security import safe_str_cmp
from user import User


def authenticate(username, password):
    # retrieve user, which gets used to generate JWT token
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    # 'identity' should be wht you returned in the authenticate func
    user_id = payload['identity']
    return User.find_by_id(user_id)
