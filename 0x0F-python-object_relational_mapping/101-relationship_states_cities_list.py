#!/usr/bin/python3
"""
Print all City objects and State from hbtn_0e_101_usa
using SQLAlchemy,

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = (
            session.query(State)
            .order_by(State.id).all()
    )

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
