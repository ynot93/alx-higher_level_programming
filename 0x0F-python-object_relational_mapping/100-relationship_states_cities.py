#!/usr/bin/python3
"""
Print all City objects by State from hbtn_0e_6_usa
using SQLAlchemy,

"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = State(name='California', cities=[City(name='San Francisco')])

    session.add(state)
    session.commit()
    session.close()
