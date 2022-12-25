#!/usr/bin/env python3
'''
Prints all City objects from the database hbtn_0e_14_usa.

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

    # Create states and cities tables
    Base.metadata.create_all(engine)

    # Create session for performing CRUD operations on database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create State and City objects.
        c1 = City(name='San Francisco')
        s1 = State(name='California')
        # Add related City object
        s1.cities.append(c1)
        # Add to session
        session.add(s1)  # c1 implicitly added by save-update cascade.
        # Commit to database
        session.commit()
    except Exception as e:
        raise e
    finally:
        session.close()
