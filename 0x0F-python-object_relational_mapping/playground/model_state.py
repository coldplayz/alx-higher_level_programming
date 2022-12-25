#!/usr/bin/env python3
'''
Contains the class definition of
a State and an instance Base = declarative_base().
'''
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''
engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()
'''

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True)  # auto increments by default
    name = Column(String(128), nullable=False)
