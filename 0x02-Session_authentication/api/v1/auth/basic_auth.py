#!/usr/bin/env python3
""" Auth class, Require auth with stars """
from flask import request
from base64 import b64decode
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """"" Extract user credentials"""
        if decoded_base64_authorization_header is None or type(
                decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user = decoded_base64_authorization_header.split(':')
        return user[0], user[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """"" User object from credentials"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"" Current user"""
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            credentials = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(credentials[0],
                                                     credentials[1])
            return user
        except Exception:
            return None
