from Objects.Location import Location
import Configuration as cfg


class CInterpreter:

    def __init__(self):
        print("Welcome to Climate Change Game Changer.")

    def readUserInput(self, userInput, player, room):
        if "quit" in userInput.lower():
            return False
        elif "right" in userInput.lower():
            if player.getLocation().x+1 <= cfg.dimensions[0]-1:
                player.setLocation(Location(player.getLocation().x+1, player.getLocation().y))
        elif "left" in userInput.lower():
            if player.getLocation().x-1 >= 0:
                player.setLocation(Location(player.getLocation().x-1, player.getLocation().y))
        elif "up" in userInput.lower():
            if player.getLocation().y-1 >= 0:
                player.setLocation(Location(player.getLocation().x, player.getLocation().y-1))
        elif "down" in userInput.lower():
            if player.getLocation().y + 1 <= cfg.dimensions[1] - 1:
                player.setLocation(Location(player.getLocation().x, player.getLocation().y+1))
        elif "talk" in userInput.lower():
            if room.npc != None:
                while True:
                    print(room.npc.getResp())
                    userInput = input("True or False? ")
                    if "bye" in userInput.lower():
                        room.npc.resetPos()
                        break
                    else:
                        if room.npc.answer(userInput):
                            player.updateScore()
                            room.npc.setFlag()
        return True