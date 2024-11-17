#!/usr/bin/python3

""""

"""
import json
import os
from models.base_model import BaseModel

class FileStorgage:
    """
    This is the initialization of the class
    """

    __file_path = "file.json"
    __objectcs = {}

    def new(self, obj):
        """
        Create and stores a new object
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        To retrieve all the objects from the provite attribute
        """
        return FileStorage._objects

    def save(self):
        """
        To serialize the object dict into JSON format
        """
        all_objs = FileStorage._objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        To deserialze the object and read it
        """
        if os.path.isFile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", enconding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(",")
                        cls = eval(class_name)
                        instance = cls(**vales)
                        FileStorage.__objects[key] = instance
                    except Exception:
                        pass

