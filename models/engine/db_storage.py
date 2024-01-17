#!/usr/bin/python3
"""New class for SQLAlchemy-based database storage"""

# Import necessary modules and classes
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """Create tables in the MySQL database using SQLAlchemy"""

    # Class variables for engine and session
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database connection based on environment variables"""

        # Retrieve MySQL database connection information from environment variables
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        # Create a SQLAlchemy engine with MySQL connection details
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        # Drop all tables if the environment is set to 'test'
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of objects from the database"""

        dic = {}

        # If a specific class is provided, query objects of that class
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            # If no specific class is provided, query objects from a list of classes
            class_list = [State, City, User, Place, Review, Amenity]
            for class_obj in class_list:
                query = self.__session.query(class_obj)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """Add a new element to the session"""

        self.__session.add(obj)

    def save(self):
        """Save changes to the database"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete an element from the session and database"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configure and create tables in the database"""

        # Create tables based on defined models
        Base.metadata.create_all(self.__engine)

        # Create a scoped session for thread safety
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Close the session"""

        self.__session.close()
