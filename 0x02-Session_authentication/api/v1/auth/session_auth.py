#!/usr/bin/env python3
""" Auth class, Require auth with stars """
from flask import request
from base64 import b64decode
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """"" SessionAuth class, Require auth with stars """""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """"" Create session """""
        if user_id is None or type(user_id) is not str:
            return None
        from uuid import uuid4
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """"" User id for session id """""
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """"" Current user """""
        if request is None:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
