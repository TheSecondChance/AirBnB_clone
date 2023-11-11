#!/usr/bin/python3
"""Test File Storage instantiation"""
import unittest
import models
import os
from ...models.base_model import BaseModel
from ...models.engine.file_storage import FileStorage


class Test_FileStorage_instantiation(unittest.TestCase):
    """Test Instantiation

    Args:
        unittest: inheret from unittest
    """

    def test_FileStorage(self):
        """Test File Strorage"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_private_dict(self):
        """Test object is private dict"""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_file_with_arg(self):
        """Test file"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_init(self):
        """Test storage initialized"""
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_file_private_str(self):
        """Test file path is private"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))


class TestFileStorage(unittest.TestCase):
    """Test file storage

    Args:
        unittest: inherit from unittest
    """

    def setUp(self):
        self.json_file = "json_file.json"

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_storage_return_dictinora(self):
        """Test storage return dict"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test New Storage"""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_all_wit(self):
        """Test storage"""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_with_None(self):
        """Test New"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_reload(self):
        """Test save and reload"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertTrue(
            new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None
        )
        self.assertTrue(
            new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None
        )

    def test_save(self):
        """Test save file"""
        model = BaseModel()
        models.storage.new(model)
        models.storage.save()
        save = ""
        with open("json_file.json", "r") as file:
            save = file.read()
            self.assertIn("BaseModel." + model.id, save)

    def test_save_to_file(self):
        """Test save to file"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty(self):
        """Test empty file reload"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()

    def test_new_(self):
        """Test with arg"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)


if __name__ == "__main__":
    unittest.main()
