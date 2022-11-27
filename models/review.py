#!/usr/bin/python3
"""defines the review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """attributes of the amenity class
    place_id: unique identifier of the place under review(str)
    user_id: unique identity of the user(str)
    text: review of the place(str)
    """

class Review(BaseModel):
    place_id = ""
    user_id = ""
    review = ""
