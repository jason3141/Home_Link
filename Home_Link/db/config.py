# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
