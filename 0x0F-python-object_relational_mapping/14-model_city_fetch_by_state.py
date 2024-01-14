#!/usr/bin/python3
"""
Print all City objects by State from hbtn_0e_6_usa
using SQLAlchemy,

"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username, password, database = sys.argv[1:4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = (
            session.query(State, City)
            .filter(State.id == City.state_id)
            .order_by(City.id).all()
    )

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
