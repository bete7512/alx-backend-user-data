#!/usr/bin/env python3
""" Auth class, Require auth with stars """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    """ Basic Auth class, Require auth with stars """
