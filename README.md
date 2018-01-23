# DataManagementHSLU
Descriptive Code SQL and some Python scripts using python libaries like sqlite3 and slqAlchemy.
There will be two ways. One with SQLite and the second (more secure way) with SQLAlchemy.
All scripts are self written and not copied from third party websites.

For the main part SQL Alchemy will be used instead of SQLite. It protects against SQLInjection by default, because raw SQL input would lead so failures.

This rep includes files for:

- creating a database using SQLAlchemy
- adding a user
- selecting/searching for a member
- manipulating userdata
- deleting a member from database (not advisable but has to be done from time to time)
- a general file that holds all kinds of functions
-> main script that runs the main function

To use those files users have to install SQLAlchemy which is easiest done by a pip install: "pip install SQLAlchemy"

Beside this users have to install the following modules:
- pandas via pip 

..or using something like Anaconda
