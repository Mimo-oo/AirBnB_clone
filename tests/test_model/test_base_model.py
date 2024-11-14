#/usr/bin/python3

import unittest
from models.base.model import BaseModel

class unittest(unittest.TestCase):
    def test_init(self):
        my_model = BaseModel()
        
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        
    def test_save(self):
        my_model = Basemodel()
        current = my_model.updated_at
        update = my_model.save()
        self.assertNotEqual(current, update)

    def test_to_dict(self):
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)

        self.assertEqual(my_model_dict["__class"], 'BaseModel')
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created-at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_dict["updated_at"], my_model.updated_at.isoformat())

    def test_str(self):
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseMode]'))

        self.assertIn(my_model.id, str(my_model))




    

