#!/usr/bin/env python3
'''
Prints the State object with the name
passed as argument from the database hbtn_0e_6_usa.

SQLi-safe.
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker, mapper

if __name__ == '__main__':
    # Create engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    name = sys.argv[4]

    # Create session for performing CRUD operations on database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Get Query object representing result set.
        qobj = session.query(
                State.id).filter(State.name == name)

        id = qobj.scalar()
        if id:
            print(id)
        else:
            # Empty result set
            print("Not found")

        '''
        for row in rows:
            print(f'{row.id}: {row.name}')
        '''
    except Exception as e:
        raise e
    finally:
        session.close()
