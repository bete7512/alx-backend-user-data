#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
AUTH_TYPE = getenv("AUTH_TYPE")
if AUTH_TYPE == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ error handler for (unauthorized) 401 status code """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ error handler for (forbidden) 403 status code """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_func() -> str:
    """ before request function"""
    if auth is None:
        return
    if auth.require_auth(request.path, ['/api/v1/status/',
                                        '/api/v1/unauthorized/',
                                        '/api/v1/forbidden/',
                                        '/api/v1/auth_session/login/']):
        if auth.authorization_header(request) is None\
                and auth.session_cookie(request) is None:
            abort(401)
        if not auth.current_user(request):
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
