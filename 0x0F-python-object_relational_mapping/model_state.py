#!/usr/bin/python3
"""This script connects to SQL"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


Base = declarative_base()


class State(Base):
    """Creates a Table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


username = sys.argv[1]
password = sys.argv[2]
host = 'localhost'
port = 3306
database_name = sys.argv[3]

eng = f"mysql://{username}:{password}@{host}:{port}/{database_name}"
engine = create_engine(eng)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
