#!/usr/bin/env python3
"""BasicAuth Class that inherits from Auth
"""


from models.user import User
from typing import List, TypeVar
import base64
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth
    Methods:
        def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        def current_user(self, request=None) -> TypeVar('User'):
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None or \
            type(authorization_header) is not str or \
                not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ returns the decoded value of a Base64 string """
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None

        try:
            return base64.b64decode(
                           base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """returns the user email and password from Base64 decoded value"""
        if decoded_base64_authorization_header is None or \
            type(decoded_base64_authorization_header) is not str or \
                decoded_base64_authorization_header.find(':') == -1:
            return None, None
        email, pwd = decoded_base64_authorization_header.split(':', 1)
        return (email, pwd)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None and type(user_email) is not str:
            return None
        if user_pwd is None and type(user_pwd) is not str:
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        # Retrieve the Authorization header from requests using Auth
        auth_in_header = self.authorization_header(request)

        # Decode auth in header to retrieve user credentials using base64
        b64_header = self.extract_base64_authorization_header(auth_in_header)
        decoded_header = self.decode_base64_authorization_header(b64_header)
        # Extract user credentials and retrieve user from DB Object
        user_cred = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(user_cred[0], user_cred[1])
