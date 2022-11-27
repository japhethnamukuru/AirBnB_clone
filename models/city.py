#!/usr/bin/python3
"""definition of the city class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """city attributes based on th basemodel
        State_id: the state the city is in(str)
        name: Name of the city(str)
    """

    state_id = ""
    name = ""
