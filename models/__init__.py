#!/usr/bin/python3

"""
    This module contains unique FileStorageInstance
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

test_classes = {'BaseModel': BaseModel}

storage = FileStorage()
storage.reload()
