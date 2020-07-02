class Location:

    x = 0
    y = 0

    def __init__(self, _x = 0, _y = 0):
        self.x = _x
        self.y = _y

    def __str__(self):
        return self.x + " " + self.y