#!/usr/bin/python
"""Module that retrieve and prints the first state from a MySQl database using SQLalchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysql://{}:()@localhost/{}"
                           .format(sys.argv[1],sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    # Create  a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a session object
    session = Session()

    # Retrieve the first state from the database and print its ID and name
    state = session.query(State).order_by(State.id).first()
    if state:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))