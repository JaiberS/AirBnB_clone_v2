#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import environ
from uuid import uuid4


if "HBNB_TYPE_STORAGE" in environ.keys(
) and environ["HBNB_TYPE_STORAGE"] == "db":
    class Review(BaseModel, Base):
        """This is the class for Review
        Attributes:
        place_id: place id
        user_id: user id
        text: review description
        """
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

        def __init__(self, **kwargs):
            setattr(self, "id", str(uuid4()))
            for k, v in kwargs.items():
                setattr(self, k, v)
else:
    class Review(BaseModel):
        """This is the class for Review
        Attributes:
        place_id: place id
        user_id: user id
        text: review description
        """
        place_id = ""
        user_id = ""
        text = ""
