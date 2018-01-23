from sqlalchemy.sql import select
from random import randint
import datetime
import os
from sqlalchemy import MetaData, Table, create_engine

metadata = MetaData()

# functions to check input str/int before those values go into the database
def typecheck(inputvalue, inputkind):
    if inputkind == "str":
        try:
            int(inputvalue) / 2
            #print('value is a number')
            return True
        except:
            #print('value is a string, thank you ')
            return False
    elif inputkind == "int":
        try:
            int(inputvalue) / 2
            #print('value is a number, thank you ')
            return False
        except:
            #print('value is a string')
            return True
    else:
        print('No valid input, please enter either "str" or "int"')

def inputcheck(inputvalue_test, kind):
    while typecheck(inputvalue_test, kind) == True:
        inputvalue_test = input('please enter: ' + kind)
    return inputvalue_test

# functions to check is database/file already exists
def check_file_exists(filename):
    return os.path.isfile(filename)

def check_file_loop(filename):
    while check_file_exists(filename) == False:
        filename = input('please enter an existing database inlcl .db <name.db>')
    return filename

def new_member(databasename, first_value, last_value, birth_value, email_value, phone_value, plz_value, city_value, street_value, street_num_value, pk_member,
               pk_contact, pk_address, pk_city, pk_plz, timestamp):

    engine = create_engine('sqlite:///' + databasename)
    connection = engine.connect()
    
    # loads all the tables. this is important for further database input
    member = Table('member', metadata, autoload=True, autoload_with=engine)
    contact = Table('contact', metadata, autoload=True, autoload_with=engine)
    plz = Table('plz', metadata, autoload=True, autoload_with=engine)
    city = Table('city', metadata, autoload=True, autoload_with=engine)
    address = Table('address', metadata, autoload=True, autoload_with=engine)

    ins_member = member.insert().values(first_name=first_value, last_name=last_value, date_birth=birth_value, pk_member_id=pk_member,
        fk_contact_id=pk_contact, fk_address_id=pk_address, timestamp_creation=timestamp, timestamp_update=timestamp)
    ins_contact = contact.insert().values(pk_contact_id=pk_contact, emailaddress=email_value, phonenumber=phone_value,
        fk_member_id=pk_member)
    ins_plz = plz.insert().values(pk_plz_id=pk_plz, plz=plz_value)
    ins_city = city.insert().values(pk_city_id=pk_city, city=city_value, fk_plz_id=pk_plz)
    ins_address = address.insert().values(pk_address_id=pk_address, street=street_value, street_num=street_num_value,
        fk_member_id=pk_member)

    connection.execute(ins_member)
    connection.execute(ins_contact)
    connection.execute(ins_plz)
    connection.execute(ins_city)
    connection.execute(ins_address)

def column_tolist(connection, table, position):
    # This functions checks if values are already in the table
    s = select([table])
    rp = connection.execute(s)
    results = rp.fetchall()

    itemlist = []
    for items in results:
        itemlist.append(items[position])
    return itemlist

def check_value(itemlist, value_check):
    print(itemlist) # only for debugging
    if value_check in itemlist:
        return False
    else:
        return True

def check_input(itemlist, uservalue):
    while check_value(itemlist, uservalue) == False:
        uservalue = randint(100000, 999999)
    return uservalue
