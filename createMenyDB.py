import sys
from sqlalchemy import
Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import
declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine


Base = declarative_base()

engine = create_engine('sqlite:///retaurantmenu.db')

Base.metadata.Create_all(engine)
