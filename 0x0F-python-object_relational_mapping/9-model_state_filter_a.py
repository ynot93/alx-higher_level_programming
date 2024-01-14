#!/usr/bin/python3
"""
Lists the first state objects from hbtn_0e_6_usa using SQLAlchemy,
that contain the letter a.

"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_with_a = session.query(State).filter(State.name.like('%a%'))
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
