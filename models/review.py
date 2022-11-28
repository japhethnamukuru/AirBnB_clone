#!/usr/bin/python3
"""
    The reviews module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        The reviews model
    """

    place_id = ""
    user_id = ""
    text = ""

