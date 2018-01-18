"""
This script uses SQLAlchemy to insert, update and delete members inside a given database
"""
from random import randint
import datetime as dt
from random import randint

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select

from create_database_sqlalchemy import create_database
from database_functions import new_member, column_tolist, check_input, check_file_loop, inputcheck

now = dt.datetime.now()
timestamp = datetime(now.year, now.month, now.day, now.hour, now.minute)
metadata = MetaData()

def add_member_database():
    # checks if database exists in working directory and throws an err if it does not
    db_nocheck = input('please enter a database name like <test.db>: ')
    database = check_file_loop(db_nocheck)

    # Code to access database and assign values to it
    create_database(database)

    # tries to connect to a database
    try:
        engine = create_engine('sqlite:///' + database)
        connection = engine.connect()
    except:
        print("database connection failed for some reason")
        print("programm will terminate now")
        quit()

    # loads all the tables. this is important for further database input
    member = Table('member', metadata, autoload=True, autoload_with=engine)
    contact = Table('contact', metadata, autoload=True, autoload_with=engine)
    plz = Table('plz', metadata, autoload=True, autoload_with=engine)
    city = Table('city', metadata, autoload=True, autoload_with=engine)
    address = Table('address', metadata, autoload=True, autoload_with=engine)

    first = input('Enter first name of new member: ')
    first_checked = inputcheck(first, 'str')

    last = input('Enter last name of new member: ')
    last_checked = inputcheck(last, 'str')

    birth = input('Enter date of birth of new member: ')
    birth_checked = inputcheck(birth, 'str')

    email = input('Enter emailaddress of new member: ')
    email_checked = inputcheck(email, 'str')

    phone = input('Enter phone number of new member: ')
    phone_checked = inputcheck(phone, 'int')

    plz_str = input('Enter plz of new member: ')
    plz_checked = inputcheck(plz_str, 'int')

    city = input('Enter city of new member: ')
    city_checked = inputcheck(city, 'str')

    street = input('Enter street of new member: ')
    street_checked = inputcheck(street, 'str')

    street_number = input('Enter street number number of new member: ')
    street_number_checked = inputcheck(street_number, 'int')

    member_id = check_input(column_tolist(connection, member, 0), randint(100000, 999999))
    contact_id = check_input(column_tolist(connection, contact, 0), randint(100000, 999999))
    plz_id = check_input(column_tolist(connection, plz, 0), randint(100000, 999999))
    city_id = check_input(column_tolist(connection, city, 0), randint(100000, 999999))
    address_id = check_input(column_tolist(connection, address, 0), randint(100000, 999999))

    # finally runs the function and adds member to database
    new_member(database, first_checked, last_checked, birth_checked, email_checked, phone_checked,
        plz_checked, city_checked, street_checked, street_number_checked, member_id, contact_id, address_id,
        city_id, plz_id, timestamp)