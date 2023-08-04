#!/usr/bin/env python3
"""
hash_password function that expects one string argument name password
and returns a salted, hashed password, which is a byte string.
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string
    Arguments:
        password: string type
    """
    paswd: bytes = password.encode('utf-8')
    return bcrypt.hashpw(paswd, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """expects 2 arguments and returns a boolean
    Arguments:
        hashed_password: bytes type
        password: string type
    """
    paswd: bytes = password.encode('utf-8')
    return bcrypt.checkpw(paswd, hashed_password)
