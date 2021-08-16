import sys

import db_table
from Tables import Session, Speaker

col = sys.argv[1]
if col == 'Room':
    col = 'Location'
val = " ".join(sys.argv[i] for i in range(2, len(sys.argv)))

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

if col == 'Speakers':
    rows = speaker_table.select(["Speakers","Session_Title"], {col:val})
    for row in rows:
        result = " ".join(str(value) for key, value in row.items())
        print(result)
else:
    rows2 = []
    res = []
    rows = session_table.select(["id", "Date", "Start", "End", "Title", "Location"], {col:val})
    for row in rows:
        tmp = session_table.select(["Parent_ID","Date", "Start", "End", "Title", "Location"],
                                   {"Parent_ID": row["id"]})
        for j in tmp:
            rows2.append(j)
    for val1 in rows:
        res.append(val1)
        for val2 in rows2:
            if val1['id'] == val2['Parent_ID']:
                res.append(val2)
    for row in res:
        if 'id' in row:
            row.pop('id')
        else:
            row.pop('Parent_ID')
        result = " ".join(str(value) for key, value in row.items())
        print(result)





