from Objects.Location import Location
class Player:

    # Instance variables
    playerName = ""
    health = 100
    location = None
    score = 0

    # constructor method
    # self -> variable belongs to specific object
    def __init__(self, _playerName, _health = 100, _location = Location()):
        self.playerName = _playerName
        self.health = _health
        self.location = _location

    def getPlayerName(self):
        return self.playerName

    def setPlayerName(self, _playerName):
        self.playerName = _playerName

    def getHealth(self):
        return self.health

    def setHealth(self, _health):
        self.health = _health

    def getLocation(self):
        return self.location

    def setLocation(self, _location):
        self.location = _location

    def getScore(self):
        return self.score

    def updateScore(self, update = 50):
        self.score += update

    # toString
    def __str__(self):
        return "Player Name: " + self.playerName + ", Health: " + str(self.health) + ", Score: " + str(self.score)