#!/usr/bin/python3

"""
    This module contatins the file storage class in the engine package
"""
import json
import models


class FileStorage:
    """
        The file storage engine class
    """

    __file_path = "file.json"
    __objects = {}

    
    # public instance methods
    def all(self, cls=None):
        """
            return the objects dict
        
        """

        if not cls:
            return self.__objects
        objects = {}
        for key in self.__objects.keys():
            if (key.split(".")[0] == cls.__name__):
                objects.update({key: self.__objects[key]})
        return objects


    def new(self, obj):
        """
            create a new object and add it the objects dict
        """

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
            save objects in the json file
        """

        temp = {}
        for id, obj in self.__objects.items():
            temp[id] = obj.to_dict()
        with open(self.__file_path, 'w') as file_obj:
            json.dump(temp, file_obj)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file_obj:
                objects = json.load(file_obj)
                for id, obj in objects.items():
                    object_instance = models.dummy_classes[obj['__class__']](**obj)
                    self.__objects[id] = object_instance

        except Exception as e:
            print(e)
