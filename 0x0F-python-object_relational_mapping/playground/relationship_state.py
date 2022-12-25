#!/usr/bin/env python3
'''
Contains the class definition of
a State and an instance Base = declarative_base().
'''
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")
