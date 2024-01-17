#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # Define a one-to-many relationship between State and City
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Getter method to retrieve cities related to the State"""
        var = models.storage.all()
        lista = []
        result = []

        # Iterate through all objects in storage
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)

            # Check if the object is an instance of City
            if city[0] == 'City':
                lista.append(var[key])

        # Filter cities related to the current State
        for elem in lista:
            if elem.state_id == self.id:
                result.append(elem)
        return result
