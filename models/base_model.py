#!/usr/bin/python3

"""
    Python OOP, the airbnb clone project. This module contains the base class for other models
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """The base model for all the other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs:
                if key == '__class__':
                    continue
                elif key in ('created_at', 'updated_at'):
                    isoformat = '%Y-%m-%dT%H:%M:%S.%f'
                    setattr(self, key, datetime.strptime(kwargs[key], isoformat))
                else:
                    setattr(self, key, kwargs[key])
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()


    def __str__(self):
        """return the string representation of the instance"""

        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """update the updated at attribute"""

        self.updated_at = datetime.now()
        model.storage.new(self)
        model.storage.save()

    def to_dict(self):
        """Return a dictionary instance"""

        new_dict = self.__dict__.copy()
        custom_dict = {}
        custom_dict.update({'__class__': self.__class__.__name__})

        for key in list(new_dict):
            if key in ('created_at', 'updated_at'):
                custom_dict.update({key: getattr(self, key).isoformat()})
            else:
                custom_dict.update({key: getattr(self, key)})
        return custom_dict

