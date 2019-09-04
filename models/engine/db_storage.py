#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import InvalidRequestError


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
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                environ['HBNB_MYSQL_USER'],
                environ['HBNB_MYSQL_PWD'],
                environ['HBNB_MYSQL_HOST'],
                environ['HBNB_MYSQL_DB']),
            pool_pre_ping=True)
        if 'HBNB_ENV' in environ.keys() and environ['HBNB_ENV'] == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        result = None
        a_dict = {}
        new_list = []
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            for j in classes:
                try:
                    result = self.__session.query(j).all()
                    if result is not None:
                        for i in result:
                            new_list.append(i)
                except InvalidRequestError:
                    pass
        else:
            result = self.__session.query(eval(cls)).all()
            if result is not None:
                for i in result:
                    new_list.append(i)
        return new_list

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
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_fact)

    def delete(self, obj=None):
        """delete an object from __objects
        """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def close(self):
        """ remove method on the private session_fact
        """
        self.__session.remove()
