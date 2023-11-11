#!/usr/bin/python3
"""Base Model
base class for all models in this hbnb clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """instatntiat object"""
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        models.storage.new(self)

    def save(self):
        """updated current date time"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def __str__(self):
        """string representation

        Returns:
            dict: representation of instances
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """change to dictionary

        Returns:
            dict: dictionary of all models
        """
        changed_dict = self.__dict__.copy()
        changed_dict["__class__"] = self.__class__.__name__
        changed_dict["created_at"] = self.created_at.isoformat()
        changed_dict["updated_at"] = self.updated_at.isoformat()

        return changed_dict
