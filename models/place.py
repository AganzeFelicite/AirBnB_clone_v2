#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from models.review import Review
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False
                     )
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False
                     )
    name = Column(String(128),
                  nullable=False
                  )
    description = Column(String(1024),
                         nullable=True
                         )
    number_rooms = Column(Integer,
                          default=0,
                          nullable=False
                          )
    number_bathrooms =Column(Integer,
                          default=0,
                          nullable=False
                          )
    max_guest = Column(Integer,
                          default=0,
                          nullable=False
                          )
    price_by_night = Column(Integer,
                          default=0,
                          nullable=False
                          )
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    amenity_ids = []
    review = relationship('Review', backref='place',
                          cascade='all, delete')
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def review(self):
            my_list = []
            all_obj = models.FileStorage.all(Review)
            for item in all_obj.items():
                if item.id == self.id:
                    my_list.append(item)
            return my_list
            