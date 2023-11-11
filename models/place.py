#!/usr/bin/python3
"""Defines module create Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place inherit from BaseModel"""

    name = ""
    user_id = ""
    city_id = ""
    price_by_night = 0
    number_bathrooms = 0
    description = ""
    number_rooms = 0
    longitude = 0.0
    max_guest = 0
    latitude = 0.0
    amenity_ids = []
