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
        self.assertIsNotEqual(current, update)

    def text_to_dict(self)t add .
    

