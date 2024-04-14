#!/usr/bin/python
"""Module that retrieves and prints the states with letter a from a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLALchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{} : {} @localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv [3]),
                           pool_pre_ping=True)
    # Create a sessionn factory
    Session = sessionmaker(bind=engine)

    # Create a sessiom object
    session = Session()

    # Retrieve the states with letter 'a' from the database and print its ID and name
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{} : {}".format(state.id, state.name))