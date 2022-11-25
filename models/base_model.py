#!/usr/bin/python3

"""
    Python OOP, the airbnb clone project. This module contains the base class for other models
"""
import uuid
import datetime


class BaseModel:
    """The base model for all the other classes"""

    def __init__(self, id, created_at, update_at):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()


    def __str__(self):
        return "[{}] ({}) ({})".format(self.__class__.__name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isformat()
