#!/usr/bin/python3
"""
Lists the first state objects from hbtn_0e_6_usa using SQLAlchemy

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

    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
