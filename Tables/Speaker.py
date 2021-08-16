class Speaker:
    #table column
    name = "Speakers"
    session_id = "Session_Title"

    def __init__(self, name, session_id):
        self.data = {
            self.name: name,
            self.session_id: session_id
        }
