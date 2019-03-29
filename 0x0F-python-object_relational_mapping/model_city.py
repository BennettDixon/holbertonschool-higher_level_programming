#!/usr/bin/python3
"""script for using sqlalchemy to model our models using ORM
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """cities class for use with sqlalchemy
        -> inherits from sqlalchemy declarative_base
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
