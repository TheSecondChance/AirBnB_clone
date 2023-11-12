#!/usr/bin/python3
"""This module file storage for hbnb clone.
"""
import json
import os


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
        hulu_items = FileStorage.__objects
        dict_item = {}
        for obj in hulu_items.keys():
            dict_item[obj] = hulu_items[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dict_item = {
                    ke: val.to_dict()
                    for ke, val in FileStorage.__objects.items()}
            json.dump(dict_item, file)

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
                    FileStorage.__objects = {
                        ke: self.classe()[ke.split(".")[0]](**kwa)
                        for ke, kwa in deserialize.items()
                    }
                except Exception:
                    pass

    def classe(self):
        """Valid classe and references be"""
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        classe = {
                "BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                "City": City,
                "Place": Place,
                "Review": Review,
                "State": State}
        return classe
