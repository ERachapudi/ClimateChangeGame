class NPC:

    responses = {}
    name = ""
    pos = 0
    flag = False
    lastQuestion = ""

    def __init__(self, _name):
        self.name = _name
        self.responses = {}

    def addResp(self, fact, isTrue):
        self.responses[fact] = isTrue

    def getResp(self):
        output = list(self.responses.keys())[self.pos]
        self.pos += 1
        if self.pos == len(self.responses):
            self.pos = 0
        self.lastQuestion = output
        return output

    def setFlag(self):
        self.flag = True

    def resetPos(self):
        self.pos = 0

    def answer(self, userAnswer):
        if userAnswer == "True":
            userAnswer = True
        elif userAnswer == "False":
            userAnswer = False
        if userAnswer == self.responses[self.lastQuestion]:
            print("That's correct")
            return True
        else:
            print("Incorrect Answer")
            return False