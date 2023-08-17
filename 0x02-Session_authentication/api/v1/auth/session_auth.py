#!/usr/bin/env python3
"""SessionAuth Class that inherits from Auth
"""


from models.user import User
from typing import List, TypeVar, Dict
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authentication Class
    """
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or type(user_id) is not str:
            return None

        session_ID: str = str(uuid.uuid4())
        self.user_id_by_session_id[session_ID] = user_id

        return session_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None and type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)
