#!/usr/bin/python3
"""Defines the place class"""
from models.base_models import BaseModel

class Place(BaseModel):
    """attributes of the place class
        city_id: unique id of the city(str)
        user_id: user unique id(str)
        name: name of the place(str)
        description: brief overview of the property(str)
        number_rooms: number of rooms in the place(0)
        number_bathrooms: bathrooms number in the place(0)
        max_guest: maximum number of guests allowed(0)
        price_by_night: price paid for the night(0)
        latitude: location of the place(0.0)
        longitude: location of the place(0.0)
        amenity_ids: unique id of amenity(0.0)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0 
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
