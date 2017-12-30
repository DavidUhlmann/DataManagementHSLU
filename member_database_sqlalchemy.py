'''
This script is the more secure version of the first python file
You need sqlAlchemy libary installed to use this
This code is more OOP stylish than the other one.
Runs only if started directly.
'''
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Member(Base):
    __tablename__ = 'tab_member'
    pk_member_id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    date_birth = Column(String(250), nullable=False)
    fk_contact_id = Column(Integer, ForeignKey('tab_contactdata.pk_contact_id'))
    fk_adresse_id = Column(Integer, ForeignKey('tab_address.pk_adress_id'))

class Contactdata(Base):
    __tablename__ = 'tab_contactdata'
    pk_contact_id = Column(Integer, primary_key=True)
    emailadress = Column(String(250), nullable=False)
    phonenumber = Column(String(250), nullable=False)
    fk_member_id = Column(Integer, ForeignKey('tab_member.pk_member_id'))

class PLZ(Base):
    __tablename__ = 'tab_plz'
    plz_id = Column(Integer, primary_key=True)
    plz = Column(String(250), nullable=False)

class City(Base):
    __tablename__ = 'tab_city'
    city_id = Column(Integer, primary_key=True)
    city = Column(String(250), nullable=False)
    fk_plz = Column(Integer, ForeignKey('tab_plz.plz_id'))

class Address(Base):
    __tablename__ = 'tab_address'
    pk_adress_id = Column(Integer, primary_key=True)
    street = Column(String(250), nullable=False)
    street_num = Column(String(250), nullable=False)
    fk_id_city = Column(Integer, ForeignKey('tab_city.city_id'))
    fk_member_number = Column(Integer, ForeignKey('tab_member.pk_member_id'))


if __name__ == "__main__":
    database_name_input = input("please give name for database in format <name.db>")

	# This creates the database
    engine = create_engine('sqlite:///'+database_name_input)
	# This line of code creates all tables inside this database (databaseengine)
    Base.metadata.create_all(engine)



