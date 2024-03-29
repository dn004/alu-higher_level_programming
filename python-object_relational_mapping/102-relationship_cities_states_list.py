#!/usr/bin/python3
"""
Module 102-relationship_cities_states_list.py
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    ls = session.query(City).order_by(City.id).all()
    for city in ls:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.commit()
    session.close()
