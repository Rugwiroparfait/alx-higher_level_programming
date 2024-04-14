#!/usr/bin/python
"""Module that searches for a state in a MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import String

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySql credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1],sys.argv[2],sys.argv[3]),
                           pool_pre_ping=True)
    # Create a sessionmaker instance
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()

    # Search for the speciefied state in the database
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
    
    # Print a msg if the state is not found
    if found is False:
        print("Not found")