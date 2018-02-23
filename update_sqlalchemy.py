'''
 Script allows user to update informations inside the database
'''
from fnmatch import fnmatchcase
from sqlalchemy.sql import update, select
from sqlalchemy import create_engine, MetaData, Table, inspect
import time
from datetime import datetime
from database_functions_sqlalchemy import inputcheck, connection_database, connection_engine, typecheck
from database_functions_sqlalchemy import check_file_loop, check_item_list, check_item_loop, update_timestamps

metadata = MetaData()
keywords = ['pk', 'fk', 'timestamp']

# this functions takes a whole table inside database
database_raw = 'member.db' # DAS MUSS AM ENDE DER USER EINGEBEN...
databasename = inputcheck(database_raw, 'str')
engine = create_engine('sqlite:///' + databasename)
connection = engine.connect()

now = time.ctime(int(time.time()))

def update_data(connection, tablename, columnname, old_value, new_value):
    u = update(tablename).where(tablename.c.columnname == old_value)
    u = u.values(columnname=(new_value))
    result = connection.execute(u)
    return result

# idea taken from Python cookbook third edition page 41
def string_comparison(stringinput, comparestring):
    return fnmatchcase(comparestring, stringinput)

# Method any taken from STOV
# https://stackoverflow.com/questions/3389574/check-if-multiple-strings-exist-in-another-string
def check_string_list(str, list):
    if any(x in str for x in list):
        return False

# DAS HIER NOCH DURCH EINE LISTCOMP ERSETZEN - WORKINGSOLUTION!!
def clean_column_names(list, keywords):
    testlist = []
    outputlist = []

    for item in list:
        if check_string_list(item, keywords) is False:
            testlist.append(item)

    for item in list:
        if item not in testlist:
            outputlist.append(item)
    return outputlist

def print_table(dictionary_columns):
    keylist = []
    print('You have the following tables where you can change data:')
    for key in dictionary_columns:
        keylist.append(str(key))
        print(key)

    return keylist

def update_members_database(databasename):

    # this functions takes a whole table inside database
    databasename = inputcheck(databasename, 'str')
    engine = create_engine('sqlite:///' + databasename)
    connection = engine.connect()

    timestamp = datetime.now
    keyword_timestamp_update = 'timestamp_update'

    member = Table('member', metadata, autoload=True, autoload_with=engine)
    contact = Table('contact', metadata, autoload=True, autoload_with=engine)
    plz = Table('plz', metadata, autoload=True, autoload_with=engine)
    city = Table('city', metadata, autoload=True, autoload_with=engine)
    address = Table('address', metadata, autoload=True, autoload_with=engine)

    list_tables = [member, contact, plz, city, address]

    # gives the relevant tables plus keys to access it further down in the program
    tables_key = {'key_member': member,
              'key_contact': contact,
              'key_plz': plz,
              'key_city': city,
              'key_address': address
              }

    # columns that the user can change checked by a function that gives all columns back
    tables_columns = {'col_member': clean_column_names(member.columns.keys(), keywords),
                      'col_contact': clean_column_names(contact.columns.keys(), keywords),
                      'col_plz': clean_column_names(plz.columns.keys(), keywords),
                      'col_city': clean_column_names(city.columns.keys(), keywords),
                      'col_address': clean_column_names(address.columns.keys(), keywords)}

    # Shows user which tables are available inside the database
    print('These are available tables:')
    for item in list_tables:
        print(item)

    # transforms items to strings
    list_tables_strings = [str(item) for item in list_tables]
    table_change = check_item_loop(list_tables_strings, 'table')

    # Shows the user available columns that he can manipulate:
    print('you have the following columns that you can change: ')
    columns_user_change = tables_columns.get('col_' + table_change)
    print(columns_user_change)

    # asks the user which one he would like to manipulate and does some checking as well
    print('You will now be asked which column you would like to change..')
    columns_change = check_item_loop(columns_user_change, 'column')

    # old and new values given by the user
    value_old = input('please input the old value: ')
    new_value = input('please input the replacement value: ')

    final_change_table = tables_key['key_'+str(table_change)]
    columns_change_final = final_change_table.c[columns_change]



    # manipulating timestamps GEHT NOCH NICHT WEGEN KEYERROR
    # DAS HIER UNTEN NOCH ZUM LAUFEN KRIEGEN WENN ALLES ANDERE FERTIG IST


    # list_values = final_change_table.columns.keys()
    # timestamp_column_list = [value for value in list_values if keyword_timestamp_update in value]
    #
    # if len(timestamp_column_list)>0:
    #     val_time_col = timestamp_column_list[0]
    #     timestamp_column = final_change_table.c[val_time_col]
    #     # s = select([final_change_table]).where(final_change_table.c[columns_change_final].like(value_old))
    #     s = select([final_change_table]).where(final_change_table.c[columns_change_final] == value_old)
    #     result_timestamp = connection.execute(s)
    #
    #     u = update(final_change_table).where(final_change_table.c[timestamp_column] != '')
    #     u = u.values({final_change_table.c[timestamp_column]: timestamp})
    #     result_timestamp = connection.execute(u)




    # changes the normal table data according to users inputs
    u = update(final_change_table).where(final_change_table.c[columns_change] == value_old)
    u = u.values({final_change_table.c[columns_change]:new_value})
    result = connection.execute(u)

    # changes timestamps if there are any so that the table keeps track of changes
    # alle PKs anzeigen, filtern der tabelle - spalte vor dem ändern nach dem alten value
    # die entsprechenden Zeilen dann den update timestamp auf das aktuelle Dateum abändern
    # für debugging Gründe erstmal nachdem die Änderungen vorgenommen wurden (wenns geht dann davor einbauen)
