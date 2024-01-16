#!/usr/bin/python3
"""This module defines the DBStorage class for HBNB project."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from os import getenv

class DBStorage:
    """This class manages storage of hbnb models in a database."""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine and session"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                .format(getenv('HBNB_MYSQL_USER', default=''),
                    getenv('HBNB_MYSQL_PWD', default=''),
                    getenv('HBNB_MYSQL_HOST', default='localhost'),
                    getenv('HBNB_MYSQL_DB', default='')),
                pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def all(self, cls=None):
        """Queries all objects of a certain class"""
        from models.base_model import BaseModel, Base
        classes = [BaseModel, User, State, City, Amenity, Place, Review]

        if cls:
            classes = [cls] if type(cls) == type else [cls.__class__]

        objects = {}
        for class_ in classes:
            for obj in self.__session.query(class_).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """Adds a new object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and reloads session."""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
