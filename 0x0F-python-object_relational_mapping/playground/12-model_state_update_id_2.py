#!/usr/bin/env python3
'''
Changes the name of a State object from the database hbtn_0e_6_usa.

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
        # Get object representing state with id=2
        state_obj = session.query(State).get(2)

        # Update name
        state_obj.name = "New Mexico"

        # Add updated State instance to session.
        session.add(state_obj)

        # Commit record to database.
        session.commit()
    except Exception as e:
        raise e
    finally:
        session.close()
