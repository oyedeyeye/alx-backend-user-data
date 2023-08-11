#!/usr/bin/env python3
"""Auth Class
"""


from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """class BasicAuth that inherits from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """returns the Base64 part of the Authorization header"""

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
    
