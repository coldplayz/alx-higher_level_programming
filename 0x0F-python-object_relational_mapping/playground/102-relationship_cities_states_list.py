#!/usr/bin/env python3
'''
Lists all City objects, and corresponding
State objects, contained in the database hbtn_0e_101_usa.

SQLi-safe.
'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker, mapper

if __name__ == '__main__':
    # Create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create session for performing CRUD operations on database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Get all cities as a Query object
        qobj = session.query(City)

        # Fetch all City objects in a list
        cities = qobj.all()

        # Print cities with related state
        for city in cities:
            state = city.state  # get related state object
            print(f'{city.id}: {city.name} -> {state.name}')
    except Exception as e:
        raise e
    finally:
        session.close()
