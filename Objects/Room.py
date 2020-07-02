class Room:

    description = ""
    location = None
    graphic = "▉"
    npc = None

    def __init__(self, _description, _location):
        self.description = _description
        self.location = _location

    def getDescription(self):
        return self.description

    def setDescription(self, _description):
        self.description = _description

    def getLocation(self):
        return self.location

    def __str__(self):
        return self.graphic.rstrip()