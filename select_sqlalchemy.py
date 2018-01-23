from sqlalchemy.sql import select
from sqlalchemy import create_engine, MetaData, Table
from datetime import datetime
import time
from pandas import DataFrame, read_sql_query
from create_database_sqlalchemy import create_database
from database_functions_sqlalchemy import new_member, column_tolist, check_input, check_file_loop
from database_functions_sqlalchemy import inputcheck, connection_database, connection_engine, typecheck

# metadata for database engine
metadata = MetaData()

def select_tabledata(connection, tablename):
    # Gives all data that a certain table contains as a
    s = tablename.select()
    rp = connection.execute(s)
    results = rp.fetchall()
    return results

def dataframe_query(tablename, connection):
    # Import is the space at the end of SQL Statement "FROM_"
    try:
        tablename = str(tablename)
        df = read_sql_query('SELECT * FROM ' + tablename, connection)
    except:
        print("Something went wrong with your SQL-query")
        quit()
    return df

def count_tables():
    # Asks the user if he wants to see/export more than one database table
    count = input('Do you want to see/export more than one table? (Yes/No):')
    count = count.lower()
    if count in ['yes', 'ye']:
        return True
    else:
        return False

def list_tables():
    # user decision if he wants to take on or more tables at a time
    decision_user = count_tables()

    if decision_user == True:
        tables = input('Please enter the tables you would like to export/see separated by a comma: ')
        try:
            tables = tables.lower()
            tables = tables.split(",")
        except:
            print('Something went wrong, sorry!')
            quit()
    else:
        tables = input('Please enter a table you would like to export/see: ')
        tables = tables.lower()
    return tables


def tables_printing(list_tables, connection):
    for item in list_tables:
        try:
            df = dataframe_query(item, connection)
            print(df)
        except:
            print('Something went wrong with this dataframe..')
            next()

def tables_excel(list_tables, connection, timestamp):
    for item in list_tables:
        df = dataframe_query(item, connection)
        df.to_excel('Exceleport{}+{}.xlsx'.format(timestamp, item))
        print('excel file {} have been exported to working directory...'.format(df))

def tables_csv(list_tables, connection, timestamp):
    for item in list_tables:
        df = dataframe_query(item, connection)
        df.to_csv('Exceleport{}+{}.csv'.format(timestamp, item))
        print('csv file {} have been exported to working directory...'.format(df))

# this switch emulation has been taken from Dan Baders Book: Python tricks p.264/365
def action_dict(operator, connection, list_tables, timestamp):
    return{
        'watch': lambda: (list_tables, connection),
        'excel': lambda: tables_excel(list_tables, connection, timestamp),
        'csv': lambda: tables_csv(list_tables, connection, timestamp),
    }.get(operator, lambda: None)()

def select_data():
    '''
    Main function inside this script
    Users can do several things like view, export to csv ect.
    '''
    database_raw = input('Please enter databasename like <name.db>: ')
    databasename = inputcheck(database_raw, 'str')
    engine = create_engine('sqlite:///' + databasename)
    connection = engine.connect()

    now = time.ctime(int(time.time()))

    # database tables for further use:
    member = Table('member', metadata, autoload=True, autoload_with=engine)
    contact = Table('contact', metadata, autoload=True, autoload_with=engine)
    plz = Table('plz', metadata, autoload=True, autoload_with=engine)
    city = Table('city', metadata, autoload=True, autoload_with=engine)
    address = Table('address', metadata, autoload=True, autoload_with=engine)

    # two tables lists for comparing and converting to dataframes later on
    tables = [str(member), str(contact), str(plz), str(city), str(address)]
    tables_frames = [member, contact, plz, city, address]

    member_database = select_tabledata(connection, member)
    contact_database = select_tabledata(connection, contact)
    plz_database = select_tabledata(connection, plz)
    city_database = select_tabledata(connection, city)
    address_database = select_tabledata(connection, address)

    print('Your database includes the following tables: ')
    print(tables)

    tables_userchoice = list_tables()

    print('Input what you would like to do with tables...')
    action = input('please choose: watch, excel, csv')

    try:
        action_dict(action, connection, tables_userchoice, now)
    except:
        print('something went wrong, sorry..')
        quit()