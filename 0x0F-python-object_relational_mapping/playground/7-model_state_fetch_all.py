#!/usr/bin/env python3
'''
Lists all State objects from the database hbtn_0e_6_usa.
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker, mapper

# Create engine
engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

# Base.metadata.create_all(engine)
# states = Base.metadata.tables['states']
# mapper(State, states)

# Create session for performing CRUD operations on database
Session = sessionmaker(bind=engine)
session = Session()

# Get Query object representing result set.
qobj = session.query(State).order_by(asc(State.id))

# Fetch all records of result set; each record will be an object reference...
# ...as the whole table was specified in the query, instead of select columns.
rows = qobj.all()

# Print each row; attributes of row, represented as an object reference,
# ...can be accessed with dot notation
for row in rows:
    print(f'{row.id}: {row.name}')
