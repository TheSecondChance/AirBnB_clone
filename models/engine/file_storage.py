#!/usr/bin/python3
"""This module file storage for hbnb clone.
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instan to json file
    deserializes json file to instan

    Returns:
        _type_: _description_
    """

    __file_path = "json_file.json"
    __objects = {}

    def new(self, obj):
        """__objects the obj with key <obj class name>.id

        Args:
            obj (_type_): _description_
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """Return dictionary __object

        Returns:
            obj: dictionary object
        """
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            obj_dict = {ke: val.to_dict() for ke, val in FileStorage.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists
        otherwise, do nothing.
        If the file doesn't exist, no exception should be raised
        """
        if not os.path.exists(FileStorage.__file_path):
            return
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    deserialize = json.load(file)
                    class_name = {"BaseModel": BaseModel}
                    FileStorage.__objects = {
                        ke: class_name[ke.split(".")[0]](**kwa)
                        for ke, kwa in deserialize.items()
                    }
                except Exception:
                    pass
