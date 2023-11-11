#!/usr/bin/python3
"""Creates User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City objects inheirt BaseModel"""

    state_id = ""
    name = ""
