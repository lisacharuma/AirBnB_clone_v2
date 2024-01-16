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
