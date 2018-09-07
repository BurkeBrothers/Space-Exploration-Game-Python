from inv import *

inventory = []

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
