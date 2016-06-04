# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class House(Base):
    __tablename__ = 'house'

    hid = sqlalchemy.Column(sqlalchemy.String, primary_key=True, name='id')
    url = sqlalchemy.Column(sqlalchemy.String)
    title = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.String)
    room = sqlalchemy.Column(sqlalchemy.String)
    htype = sqlalchemy.Column(sqlalchemy.String, name='type')
    area = sqlalchemy.Column(sqlalchemy.String)
    areaName = sqlalchemy.Column(sqlalchemy.String, name='area_name')