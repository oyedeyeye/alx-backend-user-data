#!/usr/bin/env python3
"""Auth Class
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth: class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Define which routes don't need authentication"""
        if path is None or not excluded_paths:
            return True
        for ex in excluded_paths:
            if ex.endswith('*') and path.startswith(i[:-1]):
                return False
            elif ex in {path, path + '/'}:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns  None"""
        if request is None and "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns  None"""
        return None
