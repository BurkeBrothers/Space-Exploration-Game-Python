from inv import *

rooms = {

            1 : {  "name"  : "Hall" ,
                   "east"  : 2,
                   "south" : 3 }  ,

            2 : {  "name"  : "Space Craft" ,
                   "west"  : 1,
                   "south" : 4, 
                   "item" : "Space Suit"}  ,            

            3 : {  "name"  : "Gravity Testing Room" ,
                   "north" : 1,
                   "item" : "Space Suit"}  ,

            4 : {  "name"  : "Space Suit Testing Chamber" ,
                   "north" : 2, 
                   "item" : "Space Suit"}

         }

currentRoom = 1

def showInstructions():
    #print a main menu and the commands
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")

def showStatus():
    #print the player's current status
    print("---------------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    print("---------------------------")

while(True):
    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    showInstructions()
    showStatus()

    move = input(">").lower().split()

    #if they type 'go' first
    if move[0] == "go":
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print("You can't go that way!")

    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])