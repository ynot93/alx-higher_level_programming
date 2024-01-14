#!/usr/bin/python3
"""
Print State object with name passed as argument from hbtn_0e_6_usa
using SQLAlchemy,

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

    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print(state.id)

    session.close()
