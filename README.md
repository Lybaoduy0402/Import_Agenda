### Import Agenda
This program imports the schedule of an event into a local SQLite database.

To complete this task, you will need to:
1. Open an Agenda excel file
2. Design a SQLite Database table schema allowing to store agenda information
3. Parse the content of the excel file and store the content in the table you designed

We should be able to run your program as follow:
$> ./import_agenda.py agenda.xls

Please note:
* The input file will always follow the same format as the one provided in this repository.
* We do not expect any specific output.

### Lookup Agenda
This program finds agenda sessions in the data you imported.

We should be able to run your program as follow:
$> ./lookup_agenda.py column value

Where:
* column can be one of {date, time_start, time_end, title, location, description, speaker}
* value is the expected value for that field

For example, if I got the following simplified rows:
Title	     Location 	  Description		    Type
===========================================================================
Breakfast    Lounge	  Fresh fruits and pastries Session
Hangout	     Beach	  Have fun		    Subsession of Breakfast
Lunch	     Price Center Junk food    	   	    Session
Dinner	     Mamma Linnas Italien handmade pasta    Session
Networking   Lounge	  Let's meet		    Subsession of Dinner

Then the expected behavior is as follow:
$> ./lookup_agenda.py location lounge
Breakfast   Lounge    	  Fresh fruits and pastries Session	  # Returned because its location is lounge 
Hangout	    Beach	  Have fun		    Subsession    # Returned because its parent session location is lounge
Networking  Lounge	  Let's meet   	   	    Subsession	  # Returned because its location is lounge


### db_table.py
This file provides a basic wrapper around the SQLite3 database and provides features such as:
* create table
* select
* insert
* update


This can be used as follow:
from db_table import db_table
users = db_table("users", { "id": "integer PRIMARY KEY", "name": "text", "email": "text NOT NULL UNIQUE" })
users.insert({"name": "Simon Ninon", "email": "simon.ninon@whova.com"})
users.insert({"name": "Xinxin Jin", "email": "xinxin.jin@whova.com"})
users.insert({"name": "Congming Chen", "email": "congming.chen@whova.com"})
users.select()
users.update({'name': 'John'}, {'id':2})
users.select(['name', 'email'], {'id': 2})
users.close()


### agenda.xls
This is the file you are supposed to import for the "Import Agenda" program.
We will always use the same format as the one you can observe in this file.
You may be interested to open this file and to read the instructions at the top of the excel sheet.


## Resources
* [Python SQLite3 documentation](https://docs.python.org/2/library/sqlite3.html)
* [Python Excel parsing](https://github.com/python-excel/xlrd)
