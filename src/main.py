import time

x = 0.5

def MainMenu():
    print("---Welcome to my game---")
    time.sleep(x)
    print("Start")
    time.sleep(x)
    print("Quit")
    choice = int(input("Choice: "))

    if(choice == "1"):
        Game.Main()
