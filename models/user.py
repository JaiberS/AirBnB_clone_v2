#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


if "HBNB_TYPE_STORAGE" in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class User(BaseModel, Base):
        """This is the class for user
        Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        """
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
else:
    class User(BaseModel):
        """This is the class for user
        Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
        """
        email = ""
        password = ""
        first_name = ""
        last_name = ""
