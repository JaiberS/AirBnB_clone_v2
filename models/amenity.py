#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import environ
from models.place import place_amenity
from uuid import uuid4


if "HBNB_TYPE_STORAGE" in environ.keys(
) and environ["HBNB_TYPE_STORAGE"] == "db":
    class Amenity(BaseModel, Base):
        """
        This is the state class
        """
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
#        place_amenities = relationship("Place",
#                                      secondary=place_amenity)

else:
    class Amenity(BaseModel):
        """This is the class for Amenity
        Attributes:
        name: input name
        """
        name = ""
