#!/usr/bin/python3

"""This module tests the base model class"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.obj = BaseModel()

    # testing instances
    def test_id(self):
        self.assertIs(type(self.obj.id), str)
