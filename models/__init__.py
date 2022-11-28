#!/usr/bin/python3

"""
    This module contains unique FileStorageInstance
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

test_classes = {'BaseModel': BaseModel, "User": User}

storage = FileStorage()
storage.reload()
