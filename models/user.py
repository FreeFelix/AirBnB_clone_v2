#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for your login
        first_name: first name
        last_name: last name
        places: relationship to the Place class
        reviews: relationship to the Review class
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Define a one-to-many relationship between User and Place
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")

    # Define a one-to-many relationship between User and Review
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
