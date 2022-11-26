#!/usr/bin/python3

"""
    This module contatins the file storage class in the engine package
"""
import json


class FileStorage:
    """
        The file storage engine class
    """

    __file_path = "file.json"
    __objects = {}

    
    # public instance methods
    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects.update({obj.__class__.__name__: obj})

    def save(self):
        with open(__file_path, 'a') as file_obj:
            json.dump(__objects, file_object)

    def reload(self):
        if self.__file_path:
            with open(self.file_path) as file_obj:
                __objects = json.load(file_obj)
            return __objects
        else:
            pass
