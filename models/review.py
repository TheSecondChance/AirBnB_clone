"""Defines Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Revie Clasee inherit from BaseModel"""

    text = ""
    user_id = ""
    place_id = ""
