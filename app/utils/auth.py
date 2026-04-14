from functools import wraps

from flask_login import current_user

from app.utils.response import api_response


def login_required_json(view_function):
    @wraps(view_function)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return api_response(False, "Authentication required", {}, 401)
        return view_function(*args, **kwargs)

    return wrapper
