#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import environ
from uuid import uuid4


if "HBNB_TYPE_STORAGE" in environ.keys(
) and environ["HBNB_TYPE_STORAGE"] == "db":
    class City(BaseModel, Base):
        """This is the class for City
        Attributes:
        state_id: The state id
        name: input name
        """
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities", cascade="all,delete")

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class City(BaseModel):
        """This is the class for City
        Attributes:
        state_id: The state id
        name: input name
        """
        state_id = ""
        name = ""
