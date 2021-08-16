class Session:
    #table column
    id = "id"
    date = "Date"
    start = "Start"
    end = "End"
    session = "isSession"
    title = "Title"
    location  = "Location"
    description = "Description"
    speaker = "Speakers"
    parent_id = "Parent_ID"

    def __init__(self, parent_id, date, start, end, session_title, location, description):
        self.data = {
            self.parent_id: parent_id,
            self.date: date,
            self.start: start,
            self.end: end,
            self.title: session_title,
            self.location: location,
            self.description: description,
        }
