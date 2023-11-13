import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}
    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(350), nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)
    fav_characters = relationship('Fav_characters', backref='user', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_diameter = Column(Integer)
    planet_rotation_period = Column(Integer)
    planet_orbital_period = Column(Integer)
    planet_gravity = Column(String(250))
    planet_population = Column(Integer, nullable=False)
    planet_climate = Column(String(250))
    planet_terrain = Column(String(250))
    planet_surface_water = Column(Integer)
    planet_name = Column(String(300), nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)
    
class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_height = Column(Integer, nullable=False)
    character_mass = Column(Integer)
    character_hair_color = Column(String(250))
    character_skin_color = Column(String(250))
    character_eye_color = Column(String(250))
    character_birth_year = Column(String(250))
    character_gender = Column(String(250))
    character_name = Column(String(300), nullable=False)
    fav_characters = relationship('Fav_characters', backref='user', lazy=True)
    

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


class Fav_characters(Base):
    __tablename__ = 'fav_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id')) 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
