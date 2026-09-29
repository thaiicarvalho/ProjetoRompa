from functools import wraps

from flask import session
from flask import redirect
from flask import url_for


def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):


        if "usuario_id" not in session:

            return redirect(
                url_for("auth.login")
            )

        return func(*args, **kwargs)

    return wrapper