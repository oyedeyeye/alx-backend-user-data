#!/usr/bin/env python3
"""Module for Session Authentication
"""


from api.v1.views import app_views
from flask import abort, jsonify, request
from os import getenv
from models.user import User


@app_views.route('/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def session_auth_login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
        return the JSON object with body
        -  email
        -  password
    """
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')

    if not user_email:
        return jsonify({"error": "email missing"}), 400
    if not user_pwd:
        return jsonify({"error": "password missing"}), 400

    try:
        serched_users = User.search({'email': user_email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    if not searched_users:
        return jsonify({"error": "no user found for this email"}), 404

    user = searched_users[0]
    if not user.is_valid_password(user_pwd):
        return jsonify({"error": "wrong password"}), 401
    from api.vi.app import auth
    session_cookie = getenv("SESSION_NAME")
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookies(session_cookie, session_id)
    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def session_auth_logout() -> str:
    """DELETE /api/v1/auth_session/logout
        RETURN
            False, abort(404) or
            empty JSON dictionary with status code 200
    """
    from api.v1.app import auth

    logout = auth.destroy_session(request)
    if not logout:
        abort(404)
    return jsonify({}), 200
