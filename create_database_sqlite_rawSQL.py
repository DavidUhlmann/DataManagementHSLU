'''
This file creates a simple member SQL Database using Pythons SQLite module.
Nevertheless it is not adviseable to use this code snippits in any form
It might allow SQL Injection. It is better to use some other libary like
SQLAlchemy

The database will be created inside your working directory.
You can open/edit it with DB browser for SQLite
http://sqlitebrowser.org or directly from this website via
https://github.com/sqlitebrowser/sqlitebrowser/releases
'''

import sqlite3
from sqlite3 import Error

#functions we need to work with:

def create_connection(db_file):
	'''returns a connection to some SQLite database'''
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None

def create_table(conn, create_table_sql):
	'''executes some SQL Statements'''
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def create_database(database_name):
	'''creates all the tables if they do not already exist'''
	sql_create_member_table = """ CREATE TABLE IF NOT EXISTS tab_member(
									pk_member_id INTEGER NOT NULL PRIMARY KEY,
									first_name TEXT,
									last_name TEXT,
									date_birth	TEXT,
									fk_contact_id INTEGER NOT NULL,
									fk_adresse_id INTEGER NOT NULL,
									FOREIGN KEY(fk_contact_id) REFERENCES tab_contactdata(pk_contact_id),
									FOREIGN KEY(fk_adresse_id) REFERENCES tab_adress(pk_adress_id)
									);"""
									# ON DELETE NO ACTION ON UPDATE NO ACTION has purposefully been deleted from the statement

	sql_create_contact_table = """ CREATE TABLE IF NOT EXISTS tab_contactdata(
									fk_member_id	INTEGER NOT NULL UNIQUE,
									emailadress	TEXT NOT NULL,
									phonenumber	INTEGER NOT NULL,
									pk_contact_id	INTEGER NOT NULL PRIMARY KEY,
									FOREIGN KEY(fk_member_id) REFERENCES tab_member(pk_member_id)
									);"""

	sql_create_plz_table = """ CREATE TABLE IF NOT EXISTS tab_plz(
									plz_id	INTEGER NOT NULL PRIMARY KEY,
									plz	INTEGER NOT NULL
									);"""

	sql_create_city_table = """ CREATE TABLE IF NOT EXISTS tab_city(
									city_id	INTEGER NOT NULL PRIMARY KEY,
									city	TEXT NOT NULL,
									fk_plz	INTEGER NOT NULL,
									FOREIGN KEY(fk_plz) REFERENCES tab_plz(plz_id)
									);"""

	sql_create_adress_table = """ CREATE TABLE IF NOT EXISTS tab_adress(
									fk_member_number	INTEGER NOT NULL,
									street	TEXT NOT NULL,
									street_num	TEXT NOT NULL,
									fk_id_city	INTEGER NOT NULL,
									pk_adress_id	INTEGER NOT NULL PRIMARY KEY,
 									FOREIGN KEY(fk_id_city) REFERENCES tab_city(city_id)
									);"""

	# Change tables for cheanges the user made
	# Afterwards changes can be looked up to make clear what has been changed
	# inside most companies this has to be done because of SOX/compliance issues

	sql_create_member_change_table = """ CREATE TABLE IF NOT EXISTS tab_changes_member (
										pk_change_memberdata	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
										fk_member_id	INTEGER NOT NULL,
										firstname_old	TEXT,
										firstname_new	TEXT,
										last_name_old	TEXT,
										last_name_new	TEXT,
										date_birth_old	TEXT,
										date_birth_new	TEXT,
										FOREIGN KEY(fk_member_id) REFERENCES tab_member(pk_member_id) ON DELETE NO ACTION ON UPDATE NO ACTION
										);"""

	sql_create_contact_change_table = """ CREATE TABLE IF NOT EXISTS tab_changes_contactdata (
											pk_change_contactdata	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
											fk_contact_id	INTEGER NOT NULL,
											email_alt	TEXT,
											email_neu	TEXT,
											phone_neu	INTEGER,
											phone_alt	INTEGER,
											FOREIGN KEY(fk_contact_id) REFERENCES tab_contactdata(pk_contact_id) ON DELETE NO ACTION ON UPDATE NO ACTION
										);"""

	sql_create_city_changes_table = """ CREATE TABLE IF NOT EXISTS tab_changes_city (
											pk_change_city	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
											fk_city_id	INTEGER NOT NULL,
											city_old	TEXT,
											city_new	TEXT,
											FOREIGN KEY(fk_city_id) REFERENCES tab_city(city_id) ON DELETE NO ACTION ON UPDATE NO ACTION
										);"""

	sql_create_plz_changes_table = """ CREATE TABLE IF NOT EXISTS tab_change_plz (
											pk_change_plz	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
											fk_plz_id	INTEGER NOT NULL,
											plz_neu	INTEGER,
											plz_alt	INTEGER,
											FOREIGN KEY(fk_plz_id) REFERENCES tab_plz(plz_id) ON DELETE NO ACTION ON UPDATE NO ACTION
										);"""

	tables_create = [sql_create_member_table,
					sql_create_contact_table,
					sql_create_plz_table,
					sql_create_city_table,
					sql_create_adress_table,
					sql_create_member_change_table,
					sql_create_contact_change_table,
					sql_create_city_changes_table,
					sql_create_plz_changes_table]

	conn = create_connection(database_name)
	if conn is not None:
		for element in tables_create:
			create_table(conn, element)
	else:
		print("Error, cannot connect to database!")

if __name__ == "__main__":
	database_name_input = input("please give name for database in format <name.db>")
	create_database(database_name_input)



