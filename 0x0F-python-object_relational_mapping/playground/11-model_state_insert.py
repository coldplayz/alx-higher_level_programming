#!/usr/bin/env python3
'''
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.

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

    new_state_name = 'Louisiana'
    new_state_object = State(name=new_state_name)

    # Create session for performing CRUD operations on database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Add new State instance - new record in states table - to session.
        session.add(new_state_object)

        # Commit new record to database.
        session.commit()

        print(new_state_object.id)
    except Exception as e:
        raise e
    finally:
        session.close()
