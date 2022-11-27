#!/usr/bin/python3
"""User class definition"""
from models.base_model import BaseModel

class User(BaseModel):
    """provides attributes of the class user

        email: user email address(str)
        password: user password(str)
        first_name: user first name(str)
        last_name: user last name(str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
