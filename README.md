# DataManagementHSLU
Descriptive Code SQL and some Python scripts using python libaries like slqAlchemy.
All scripts are self written and not copied from third party websites.

For the main part SQL Alchemy will be used instead of SQLite. It protects against SQLInjection by default, because raw SQL input would lead so failures.

This rep includes files for:

- creating a database using SQLAlchemy
- adding a user
- selecting/searching for a member
- manipulating userdata
- a general file that holds all kinds of functions
-> main script that runs the main function

To use those files users have to install SQLAlchemy which is easiest done by a pip install: "pip install SQLAlchemy"

Beside this users have to install the following modules:
- pandas via pip 

..or using something like Anaconda

Pleas be advised that this code has been written for a university course. It still lacks some basic exception handling and update for timestamps. This code is by far not production ready and is only for illustrating issues.
It still works if you run the main file, but does have some DRY weaknesses etc.
