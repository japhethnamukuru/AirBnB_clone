#!/usr/bin/python3

"""This module tests the base model class"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
import re


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.obj = BaseModel()
        self.obj1 = BaseModel()

    # testing instance attributes
    def test_instance_id(self):
        obj = self.obj
        obj1 = self.obj1
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertNotEqual(obj, obj1)
        match = re.fullmatch(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', obj.id)
        self.assertTrue(match)

    def test_instance_created_at(self):
        obj = self.obj
        self.assertIsInstance(obj.created_at, datetime)

    def test_instance_updated_at(self):
        obj = self.obj
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_str(self):
        obj = self.obj
        sample = "[{}] ({}) ({})".format("BaseModel", obj.id, obj.__dict__)
        self.assertEqual(str(obj), sample)

    def test_save(self):
        obj = self.obj
        test_data = obj.save()
        self.assertIsInstance(test_data, datetime)

    def test_to_dict(self):
         obj = self.obj
         test_dict = obj.to_dict()
         self.assertTrue("__class__" in test_dict)
         self.assertIsInstance(test_dict["__class__"], str)
         self.assertTrue("id" in test_dict)
         self.assertIsInstance(test_dict["id"], str)
         self.assertTrue("created_at" in test_dict)
         self.assertIsInstance(test_dict["created_at"], str)
         self.assertTrue("updated_at" in test_dict)
         self.assertIsInstance(test_dict["updated_at"], str)
         obj.number = 89
         test_dict = obj.to_dict()
         self.assertTrue("number" in test_dict)


    def test_from_dict(self):
        obj = self.obj.to_dict()
        new_obj = BaseModel(**obj)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertTrue('__class_' not in new_obj.__dict__)
        self.assertTrue(hasattr(new_obj, 'id'))
        self.assertTrue(hasattr(new_obj, 'created_at'))
        self.assertTrue(hasattr(new_obj, 'updated_at'))
        new_obj.number = 89
        self.assertTrue(hasattr(new_obj, 'number'))

        # type instances
        self.assertIsInstance(new_obj.id, str)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)

