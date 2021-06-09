import global_settings
from game import game
global_settings.init()

while(True): # samuel
    mode = 0
    print("1. human against human")
    print("2. human against ai")
    print("3. exit")
    while(True):
        userinput = input("choose which mode to play: ")
        if(userinput == "1"):
            mode = 1
            break
        elif(userinput == "2"):
            mode = 2
            break
        elif(userinput == "3"):
            mode = 3
            break
        else:
            print("please enter valid input\n")
    if(mode == 1):
        turn = 0
        while(True):
            print("1. player_one")
            print("2. player_two")
            userinput = input("which player should start, one or two? ")
            if( userinput == "1"):
                turn = 1
                break
            elif( userinput == "2"):
                turn = 0
                break
            else:
                print("please enter either 1 or 2\n")
        playerturn = turn
        while(True):
            print("1. with stealing")
            print("2. without stealing")
            userinput = input("play with or without stealing? ")
            if( userinput == "1"):
                stealing = 1
                break
            elif( userinput == "2"):
                stealing = 0
                break
            else:
                print("please enter either 1 or 2\n")
        game(0,0)
    elif(mode == 2):
        turn = 0
        while(True):
            print("1. human")
            print("2. ai")
            userinput = input("which player should start, human or ai? ")
            if( userinput == "1"):
                turn = 1
                break
            elif( userinput == "2"):
                turn = 0
                break
            else:
                print("please enter either 1 or 2\n")
        playerturn = turn
        while(True):
            print("1. with stealing")
            print("2. without stealing")
            userinput = input("play with or without stealing? ")
            if( userinput == "1"):
                stealing = 1
                break
            elif( userinput == "2"):
                stealing = 0
                break
            else:
                print("please enter either 1 or 2\n")
        while(True):
            print("1. easy (depth=2)")
            print("2. medium (depth=6)")
            print("3. hard (depth=10)")
            userinput = input("choose the ai difficulty: ")
            if( userinput == "1"):
                print("\nai is on easy difficulty\n")
                game(0,1, global_settings.easy)
                break
            elif( userinput == "2"):
                print("\nai is on medium difficulty\n")
                game(0,1, global_settings.medium)
                break
            elif( userinput == "3"):
                print("\nai is on hard difficulty\n")
                game(0,1, global_settings.hard)
                break
            else:
                print("please enter either 1 ,2 or 3\n")
    
    elif(mode == 3):
        print("we hope you liked the game")
        break
    print("//////////////////////////////////////////")
    print("//////////////////////////////////////////")
    print("//////////////////////////////////////////")
    print("\n")

# state = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
# Maxmin(state,8,0)
# state = [2,1,0,1,4,0,11,3,2,0,0,1,10,13]
# makemove(state,12,0,0)

