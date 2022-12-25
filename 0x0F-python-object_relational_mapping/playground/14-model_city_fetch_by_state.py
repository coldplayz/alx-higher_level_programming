#!/usr/bin/env python3
'''
Prints all City objects from the database hbtn_0e_14_usa.

SQLi-safe.
'''
import sys
from model_state import Base, State
from model_city import City
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
        # Get Query object representing result set..
        qobj = session.query(State.name, City.id, City.name).join(City)

        # Fetch all rows in result set
        rows = qobj.all()

        # Print result set.
        for row in rows:
            print(f'{row[0]}: ({row[1]}) {row[2]}')
    except Exception as e:
        raise e
    finally:
        session.close()
