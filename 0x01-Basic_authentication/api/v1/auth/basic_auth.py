#!/usr/bin/env python3
""" Auth class, Require auth with stars """
from flask import request
from base64 import b64decode
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class, Require auth with stars """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """"" Extract base64 authorization header"""
        if authorization_header is None or type(
                authorization_header) is not str:
            return None
        if authorization_header[:6] != "Basic ":
            return None
        base = authorization_header.split(' ')
        return base[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """"" Decode base64 authorization header"""
        if base64_authorization_header is None or type(
                base64_authorization_header) is not str:
            return None
        try:
            baseEncode = base64_authorization_header.encode('utf-8')
            baseDecode = b64decode(baseEncode)
            decodedValue = baseDecode.decode('utf-8')
            return decodedValue
        except Exception:
            return None
