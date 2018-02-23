from sqlalchemy import (Table, Column, Integer, Numeric, String, ForeignKey, DateTime, ForeignKey, Index, create_engine,
                        MetaData, insert)

from datetime import datetime

def create_database(name_database):
    metadata = MetaData()

    member = Table('member', metadata, Column('pk_member_id', Integer(), primary_key=True),
                   Column('first_name', String(25), index=True), Column('last_name', String(25), nullable=False),
                   Column('date_birth', String(12), nullable=False),
                   Column('timestamp_creation', DateTime(), default=datetime.now, nullable=False),
                   Column('timestamp_update', DateTime(), default=datetime.now, onupdate=datetime.now, nullable=False),
                   Column('fk_contact_id', ForeignKey('contact.pk_contact_id')),
                   Column('fk_address_id', ForeignKey('address.pk_address_id')), )

    contact = Table('contact', metadata, Column('pk_contact_id', Integer(), primary_key=True),
                    Column('emailaddress', String(255), nullable=False, unique=True),
                    Column('phonenumber', Integer(), nullable=False, unique=True),
                    Column('fk_member_id', ForeignKey('member.pk_member_id'), nullable=False))

    plz = Table('plz', metadata, Column('pk_plz_id', Integer(), primary_key=True),
                Column('plz', String(255), nullable=False, unique=True))

    city = Table('city', metadata, Column('pk_city_id', Integer(), primary_key=True),
                 Column('city', String(255), nullable=False),
                 Column('fk_plz_id', ForeignKey('plz.pk_plz_id'), nullable=False))

    address = Table('address', metadata, Column('pk_address_id', Integer(), primary_key=True),
                    Column('street', String(255), nullable=False), Column('street_num', Integer(), nullable=False),
                    Column('fk_member_id', ForeignKey('member.pk_member_id'), nullable=False))

    # create_all method checks by default if the database & string(string)ucture already
    # exists & does not act if so! No SQL Code like "if not exists" needed here
    engine = create_engine('sqlite:///' + name_database)
    metadata.create_all(engine)
    print("All tables created and/or loaded")
    return engine
