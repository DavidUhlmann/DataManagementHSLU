'''
This is the main file which takes functions from the other files

'''
from sqlalchemy.sql import delete
from sqlalchemy.sql import update, select
from sqlalchemy import create_engine, MetaData, Table, inspect
import time
from datetime import datetime
from database_functions_sqlalchemy import inputcheck, connection_database, connection_engine, typecheck, ask_user_database
from database_functions_sqlalchemy import check_file_loop, check_item_list, check_item_loop, update_timestamps

from update_sqlalchemy import update_members_database
from create_database_sqlalchemy import create_database
from select_sqlalchemy import select_whole_tables
from add_members_sqlalchemy import add_member_database

VALUE_USER_DECISION = ['update', 'show', 'add']

def get_database_name():
    print('please input the name of the database you would like to open like: <database.db>')
    database_name = input('please enter name here: ')
    return database_name

def manipulate_database():
    print('what would like to do with your existing database: \n')
    print('You have the following options: \n')
    print('Update member information (update): \n')
    print('Show database information (show): \n')
    print('Add new member information (add): \n')
    user_input = input('Please input your choice: ')
    return user_input.lower()

def get_value_func(value, list):
    if value in list:
        return True
    else:
        print('no valid input, please correct: ')
        return False

def exit_script():
    exit_user = input('Would you like to continue? (Yes/No:')
    if exit_user in ['Yes', 'yes', 'YES', 'YES']:
        return True
    else:
        return False

def main():
    while True:
        exit_program_user = input('Would you like to quit this program? (YES/NO)?: ')
        if exit_program_user in ['Yes', 'yes', 'ye', 'YES', 'Ye']:
            return False
        else:
            while True:
                '''this is the part where the script runs:'''
                print('You do have basically four options right now: \n')
                print('Create a database (1):\n')
                print('Open an existing database and do stuff with it (2): \n')
                user_decision = input('Please what you would like to do? (1 or 2): \n')

                if user_decision == str(1):
                    database_name = get_database_name()
                    create_database(database_name)
                    return True
                elif user_decision == str(2):
                    database_name = get_database_name()
                    manipulation_dec = manipulate_database()

                    while get_value_func(manipulation_dec, VALUE_USER_DECISION) == False:
                        manipulation_dec = manipulate_database()

                    if manipulation_dec == 'update':
                        update_members_database(database_name)
                    elif manipulation_dec == 'show':
                        select_whole_tables(database_name)
                    else:
                        add_member_database(database_name)
                else:
                    print('your input did not match criteria, program will end now..')
                    return True
                    quit()

                print('Would you like to exit script? (Yes/No): \n')
                dec_user_break = input('Please choose:')

                if dec_user_break in ['Yes', 'yes', 'YES']:
                    break


# runs if script is run directly
if __name__ == '__main__':
    main()