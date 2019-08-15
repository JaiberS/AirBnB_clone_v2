#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
import models
from uuid import uuid4



if "HBNB_TYPE_STORAGE" in environ.keys() and environ["HBNB_TYPE_STORAGE"] == "db":
    class State(BaseModel, Base):
       """
       This is the state class
       """
       __tablename__ = 'states'
       name = Column(String(128), nullable=False)
       cities = relationship("City", backref="state")
       def __init__(self, **kwargs):
           setattr(self, "id", str(uuid4()))
           for k, v in kwargs.items():
               setattr(self, k, v)
else:
    class State(BaseModel):
        """
        this is the state class
        """
        name = ""

        @property
        def cities(self):
            all_cities = models.storage.all(City)
            lista = []
            keys = all_cities.items()
            for i, j in keys:
                if "City" == i[0:4] and j.state_id == self.id:
                    lista.append(j)
            return(lista)
