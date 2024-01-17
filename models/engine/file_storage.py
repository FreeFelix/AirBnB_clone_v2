#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

# Import necessary modules and classes
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: dictionary to store instances
    """
    # Class variables for the file path and objects
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of objects filtered by class"""
        dic = {}

        # If a specific class is provided, filter objects by that class
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if partition[0] == cls.__name__:
                    dic[key] = self.__objects[key]
            return dic
        else:
            # If no specific class is provided, return all objects
            return self.__objects

    def new(self, obj):
        """Adds a new instance to the dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes instances to the JSON file"""
        my_dict = {}

        # Convert instances to dictionary format
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()

        # Save the dictionary to the JSON file
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes JSON file to instances"""
        try:
            # Load instances from the JSON file to the dictionary
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete an existing instance from the dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """Calls reload() to load instances from the JSON file"""
        self.reload()
