#!/usr/bin/python3

"""
    This module contains unique FileStorageInstance
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
