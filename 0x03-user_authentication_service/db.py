#!/usr/bin/env python3
"""DB module """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """ DB class """

    def __init__(self) -> None:
        """ Initialize a new DB instance """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Memoized session object """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """  save the user to the database and returns a User object """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        print(user)
        return user
    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users table"""
        if not kwargs:
            raise InvalidRequestError

        cols = ["id", "email", "hashed_password", "session_id", "reset_token"]

        for arg in kwargs:
            if arg not in cols:
                raise InvalidRequestError

        found = self._session.query(User).filter_by(**kwargs).first()

        if found:
            return found
        else:
            raise 