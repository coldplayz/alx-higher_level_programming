#!/usr/bin/env python3
'''
Contains the class definition of
a City.
'''
from sqlalchemy import Integer, String, Column, ForeignKey
from relationship_state import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
