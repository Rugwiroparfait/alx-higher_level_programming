#!/usr/bin/python3
"""Module that retrieve and prints all states and prints all states from a MySQL database with SQLalchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import state

if __name__ == "__main__":
    # Create The SQLAlchemy engine using the provided MySQL credential
    engine = create_engine("mysql+mysql://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3],
                            pool_pre_ping=True))
    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Retrieve alll states from the database and print their IDs and name
    for state in session.query(state).order_by(state.id):
        print("{}: {}".format(state.id, state.name))