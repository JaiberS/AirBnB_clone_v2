#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(environ['HBNB_MYSQL_USER'], environ['HBNB_MYSQL_PWD'], environ['HBNB_MYSQL_HOST'], environ['HBNB_MYSQL_DB']), pool_pre_ping=True)
        if environ['HBNB_ENV'] == "test":
            MetaData().drop_all(self.__engine)
 
    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        if cls is None:
            result = self.__session.query(User, State, City, Amenity, Place, Review)
        else:
            result = self.__session.query(cls)
        a_dict = {}
        for i in result:
            a_dict.setdefault(i.name + "." + str(i.id), i)
        return a_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj is not None:
            self.__session.add(obj)
            self.__session.commit()

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_fact)

    def delete(self, obj=None):
        """delete an object from __objects
        """
        if obj is not None: 
            self.__session.delete(obj)
            self.__session.commit()
