#Import Agenda
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

To complete this task, you will need to:
1. Parse the command line arguments to retrieve the conditions that the sessions we are looking for must match.
2. Lookup the data you imported for the matching records
3. Print the result onto the screen

We should be able to run your program as follow:
$> ./lookup_agenda.py column value

Where:
* column can be one of {date, time_start, time_end, title, location, description, speaker}
* value is the expected value for that field

### db_table.py
This file provides a basic wrapper around the SQLite3 database and provides features such as:
* create table
* select
* insert
* update

These operations should be enough for this assignment, but feel free to modify if you feel the need to.

### agenda.xls
This is the file you are supposed to import for the "Import Agenda" program.
We will always use the same format as the one you can observe in this file.
You may be interested to open this file and to read the instructions at the top of the excel sheet.

## Resources
* [Python SQLite3 documentation](https://docs.python.org/2/library/sqlite3.html)
* [Python Excel parsing](https://github.com/python-excel/xlrd)
