#!/usr/bin/env python3
'''
Deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa.

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

    # Create session for performing CRUD operations on database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Delete potentially multiple records.
        session.query(State).filter(
                State.name.like('%a%')).delete(synchronize_session='fetch')

        # Commit changes to database.
        session.commit()
    except Exception as e:
        raise e
    finally:
        session.close()
