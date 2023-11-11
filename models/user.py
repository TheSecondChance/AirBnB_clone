#!/usr/bin/python3
"""Creates User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Create user

    Args:
        BaseModel (classs): inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
