#!/usr/bin/python3
"""script to list all state objects using sqlalchemy
"""
from model_state import Base, State

from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    state_name = sys.argv[4]
    # create custom session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new custom session class
    session = Session()
    # find states matching state_name
    states = session.query(State)\
                    .filter(State.name == state_name)\
                    .order_by(State.id)
    if (states is not None and states.count() > 0):
        for state in states:
            print('{}'.format(state.id))
    else:
        print('Not found')
