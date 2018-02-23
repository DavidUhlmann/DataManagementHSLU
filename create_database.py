from sqlalchemy import MetaData 
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey 
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey  
from sqlalchemy import Index
from sqlalchemy import create_engine 

#non SQL imports
from datetime import datetime 

def create_user_database(name):

	metadata = MetaData()

	member = Table('member', metadata,
		Column('pk_member_id', Integer(), primary_key=True),
		Column('first_name', String(25), index=True),
		Column('last_name',String(25)),
		Column('date_birth', String(12)),
		Column('timestamp_creation', DateTime(), default=datetime.now),
		Column('timestamp_update', DateTime(), default=datetime.now, onupdate=datetime.now),
		Column('fk_contact_id', ForeignKey('contact.pk_contact_id')),
		Column('fk_address_id', ForeignKey('address.pk_address_id')),
		)

	contact = Table('contact', metadata,
		Column('pk_contact_id', Integer(), primary_key=True),
		Column('emailaddress', String(255), nullable=False),
		Column('phonenumber', Integer(), nullable=False),
		Column('fk_member_id', ForeignKey('member.pk_member_id'))
		)

	plz = Table('plz', metadata,
		Column('pk_plz_id', Integer(), primary_key=True),
		Column('plz', Integer(), nullable=False)
		)

	city = Table('city', metadata,
		Column('pk_city_id', Integer(), primary_key=True),
		Column('city', String(255), nullable=False),
		Column('fk_plz_id', ForeignKey('plz.pk_plz_id'))
		)

	address = Table('address', metadata,
		Column('pk_address_id', Integer(), primary_key=True),
		Column('street', String(255), nullable=False),
		Column('street_num', Integer(), nullable=False),
		Column('fk_member_id', ForeignKey('member.pk_member_id'))
		)

	# create_all method checks by default if the database & structure already
	# exists & does not act if so! No SQL Code like "if not exists" needed here
	engine = create_engine('sqlite:///'+name)
	metadata.create_all(engine)







