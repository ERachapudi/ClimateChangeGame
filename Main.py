import random as r
from Player import Player
import Configuration as cfg
from CInterpreter import CInterpreter as CI
from Objects.Room import Room
from Objects.Location import Location
from Objects.NPC import NPC
import sys
map = []


def main():
    ci = CI()
    createMap(cfg.dimensions[0], cfg.dimensions[1])
    playerName = input("Enter a character name: ")
    player = Player(playerName)
    run(player, ci)


def run(player, ci):
    running = True
    while running:
        updateMap(player)
        running = ci.readUserInput(input("Enter your command: "), player, getCurrentRoom(player))
        hasWon(player)


def createMap(x, y):
    global map
    npc_prob = 50
    map = []
    map.append([])
    for i in range(x):
        for j in range(y):
            if r.randint(0, 100) < npc_prob:
                map[i].append(Room("", Location(j, i)))
            else:
                room = Room("", Location(j, i))
                room.npc = NPC(generateNewName())
                room.npc.addResp(*generateFacts())
                room.setDescription("This Room has " + room.npc.name + " in it. Type 'bye' to leave the conversation.")
                map[i].append(room)
        map.append([])
    map.remove([])


def updateMap(player):
    global map
    clearScreen()
    print(player)
    displayRoom(player.getLocation().x, player.getLocation().y)
    for rooms in map:
        output = ""
        for room in rooms:
            if player.getLocation().x == room.getLocation().x and player.getLocation().y == room.getLocation().y:
                room.graphic = 'P'
            output += room.graphic + " "
            room.graphic = "▉"
        print(output.rstrip())


def displayRoom(x, y):
    global map
    if map[x][y].npc != None:
        print(map[x][y].getDescription())


def getCurrentRoom(player):
    global map
    return map[player.getLocation().x][player.getLocation().y]

def clearScreen():
    print("\n"*80)

def hasWon(player):
    if player.getScore() >= cfg.scoreToWin and player.getLocation().x == cfg.dimensions[0]-1 and player.getLocation().y == cfg.dimensions[1]-1:
        print("You have won the game. Good Job!")
        input("Press any key to exit.")
        sys.exit("Hope you had fun!")

def generateNewName():
    with open("Resources\\Names.txt", "r") as n:
        names = n.readlines()
        return r.choice(names).rstrip()

def generateFacts():
    prob = r.randint(1,100)
    if prob >= 50:
        with open("Resources\\Facts.txt", "r", newline = "") as f:
            facts = f.read()
            facts_list = facts.split("\n")
            f.close()
            return r.choice(facts_list).rstrip(), True
    else:
        with open("Resources\\FalseFacts.txt", "r", newline = "") as f:
            false_facts = f.read()
            false_facts_list = false_facts.split("\n")
            f.close()
            return r.choice(false_facts_list).rstrip(), False


if __name__ == "__main__":
    main() 