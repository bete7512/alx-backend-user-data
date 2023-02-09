#!/usr/bin/env python3
""" Auth class, Require auth with stars """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class, Require auth with stars """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """"" Extract base64 authorization header"""
        if authorization_header is None or type(authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        base = authorization_header.split(' ')
        return base[1]
