#!/usr/bin/python3
"""
Module for FilStorage unittest
"""

import unittest
import os
import json
import models

class TestFileStorage_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the FileStorage class.
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)
