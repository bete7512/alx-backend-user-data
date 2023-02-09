#!/usr/bin/env python3
""" Auth class, Require auth with stars """
from flask import request
from base64 import b64decode
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """"" SessionAuth class, Require auth with stars """""
    