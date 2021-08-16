import sys
import xlrd

import db_table
from DataModel import Session, Speaker

import_agenda = xlrd.open_workbook(sys.argv[1])
sheet = import_agenda.sheet_by_index(0)

session_object = Session.Session(None, None, None, None, None, None, None)
speaker_object = Speaker.Speaker(None, None)

session_table = db_table.db_table("sessions", { session_object.id: "integer PRIMARY KEY",
                                                session_object.parent_id: "integer",
                                                session_object.date: "string NOT NULL",
                                                session_object.start: "string NOT NULL",
                                                session_object.end: "string NOT NULL",
                                                session_object.title:"string NOT NULL",
                                                session_object.location: "string",
                                                session_object.description: "string"})
speaker_table = db_table.db_table("speakers", {speaker_object.name: "string NOT NULL",
                                               speaker_object.session_id: "string NOT NULL"})

curr_session = 0

for row in range(15, sheet.nrows):
    id = row - 14

    date = str(sheet.cell_value(rowx=row, colx=0)).replace("'", "''")
    start = str(sheet.cell_value(rowx=row, colx=1)).replace("'", "''")
    end = str(sheet.cell_value(rowx=row, colx=2)).replace("'", "''")
    session = str(sheet.cell_value(rowx=row, colx=3)).replace("'", "''")
    session_title = str(sheet.cell_value(rowx=row, colx=4)).replace("'", "''")
    location = str(sheet.cell_value(rowx=row, colx=5)).replace("'", "''")
    description = str(sheet.cell_value(rowx=row, colx=6)).replace("'", "''")
    speaker = str(sheet.cell_value(rowx=row, colx=7)).replace("'", "''")

    print(id, date, start, end, session, session_title, location)

    if session == "Session":
        session_object = Session.Session(-1, date, start, end, session_title, location, description)
        session_table.insert(session_object.data)
        curr_session = id

    elif session == "Sub":
        session_object = Session.Session(curr_session, date, start, end, session_title, location, description)
        session_table.insert(session_object.data)

    if speaker:
        alist = speaker.split("; ")
        #expect all sessions where we can find this speaker, even though he may not be the only speaker.
        for name in alist:
            speaker_object = Speaker.Speaker(name, session_title)
            speaker_table.insert(speaker_object.data)

