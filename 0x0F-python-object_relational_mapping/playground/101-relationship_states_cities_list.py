#!/usr/bin/env python3
'''
Lists all State objects, and corresponding
City objects, contained in the database hbtn_0e_101_usa.

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
        # Get all states as a Query object
        qobj = session.query(State)

        # Fetch all state objects in a list
        states = qobj.all()

        # Print states with related cities
        for state in states:
            cities = state.cities  # get list of related city objects
            print(f'{state.id}: {state.name}')
            for city in cities:
                print(f'\t{city.id}: {city.name}')
    except Exception as e:
        raise e
    finally:
        session.close()
