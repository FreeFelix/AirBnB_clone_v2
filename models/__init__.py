#!/usr/bin/python3
"""Create a unique FileStorage instance for your application"""

# Import necessary modules and classes
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

# Check the value of HBNB_TYPE_STORAGE environment variable
if getenv("HBNB_TYPE_STORAGE") == "db":
    # If set to "db", create an instance of DBStorage
    storage = DBStorage()
else:
    # Default to creating an instance of FileStorage
    storage = FileStorage()

# Reload the storage instance to load data from the storage system
storage.reload()
