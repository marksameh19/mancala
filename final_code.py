postive_infnity = float('inf')
negative_infnity = float('-inf')
stealing = 1
playerturn = 1
ai_turn = 0

def available_moves(state,player): 
        moves = []
        if(player):
            i = 0
            for move in state[0:6]:
                if(move != 0):
                    moves.append(i)
                i += 1
        else:
            i = 7
            for move in state[7:13]:
                if(move != 0):
                    moves.append(i)
                i += 1
        return moves

def get_children(state,player): 
    global ai_turn
    constant_turn = ai_turn
    children = []
    for move in available_moves(state,player):
        new_state = state[:]
        makemove(new_state,move,player,1)
        children.append([new_state,move,ai_turn])
        ai_turn = constant_turn
    return children


def Maxmin(state, depth, maximizingplayer, alpha = negative_infnity, beta = postive_infnity , counter=0) :
    global ai_turn
    counter += 1
    if depth == 0 or not(end_game(state)):
        return state[6]-state[13]
    if maximizingplayer :
        ai_turn = 1
        value = negative_infnity
        #values = []
        for child in get_children(state,1) :
            new_value = Maxmin(child[0] , depth - 1, child[2] , alpha , beta , counter)
            #values.append(new_value)
            if(new_value > value):
                value = new_value
                move = child[1]
            alpha = max(alpha , value)
            if alpha >= beta:
                break
        if(counter==1):
            return move
        #print(depth,values)
        return value
    else :
        #values = []
        value =  postive_infnity
        ai_turn = 0
        for child in get_children(state,0) :
            new_value = Maxmin(child[0] , depth - 1, child[2] , alpha , beta , counter)
            #values.append(new_value)
            if(new_value < value):
                value = new_value
                move = child[1]
            beta = min(beta , value)
            if beta <= alpha :
                break
        if(counter==1):
            return move
        #print(value)
        #print(depth,values)
        return value


def end_game (moves): 
    sideOne = 0
    sideTwo = 0
    for j in range(6):
        sideOne = int(sideOne) + int(moves[j])
        sideTwo = int(sideTwo) + int(moves[j+7])

    if(int(sideOne) == 0 or int(sideTwo) == 0):
        return False
    else:
        return True

def winning_message(moves): 
    print("")
    print("The game is over!")
    if int(moves[13]) < int(moves[6]):
        print("Player One has won the game!")
    elif int(moves[13]) > int(moves[6]):
        print("Player Two has won the game!")
    else:
        print("The game ended in a tie.")


def player_move(moves,player): 
    chosenBin = -1
    messageCode = 0
    message = " "
    invaled_input = False
    giveawayPile = -1
    while (not(invaled_input)):
        if player == 1 and  messageCode == 0:
            message = "Player One's turn..."
        elif player == 2 and messageCode == 0:
            message = "Player Two's turn..."
        elif player == 1 and messageCode == -2:
            message = "Invalid input. Try again, Player One."
        elif player == 2 and messageCode == -2:
            message = "Invalid input. Try again, Player Two."
        elif player == 1 and messageCode == -1:
            message = "You must choose a non-empty bin, Player One."
        elif player == 2 and messageCode == -1:
            message = "You must choose a non-empty bin, Player Two."

        print("")
        print(message)
        print("")

        messageCode = 0 

        if player == 1 :
            userInput = input("Enter a number to choose a bin or enter 'q' to QUIT: ")
            if userInput == "q":
                chosenBin = 13
                return chosenBin
            elif userInput == "5":
                chosenBin = 5
            elif userInput == "4":
                chosenBin = 4
            elif userInput == "3":
                chosenBin = 3
            elif userInput == "2":
                chosenBin = 2
            elif userInput == "1":
                chosenBin = 1
            elif userInput == "0":
                chosenBin = 0
            else:
                chosenBin = -2
                messageCode = -2  # invalid input

        elif player == 2 :
            userInput = input("Enter a number to choose a bin or enter 'q' to QUIT: ")
            if userInput == "q":
                chosenBin = 13
                return chosenBin
            elif userInput == "5":
                chosenBin = 7
            elif userInput == "4":
                chosenBin = 8
            elif userInput == "3":
                chosenBin = 9
            elif userInput == "2":
                chosenBin = 10
            elif userInput == "1":
                chosenBin = 11
            elif userInput == "0":
                chosenBin = 12
            else:
                chosenBin = -2
                messageCode = -2  # invalid input

        if int(chosenBin) >= 0:
            giveawayPile = moves[chosenBin]
            if int(giveawayPile) <= 0:
                messageCode = -1  # empty bin was chosen
            else :
                invaled_input = True
                return chosenBin


def makemove(state,move,player,test_mode): 
    global playerturn
    global ai_turn
    i = move
    amount = state[move]
    state[move] = 0
    while(amount):
        i += 1 
        if(player == 1 and i%14 == 13):
            continue
        if(player == 0 and i%14 == 6):
            continue
        state[i%14] += 1
        amount -= 1
    
    if(player == 1 and state[i%14] == 1 and state[(12-i)%14] != 0 and i%14 >= 0 and i%14 < 6 and stealing):
        state[6] += state[i%14]
        state[6] += state[(12-i)%14]
        state[i%14] = 0
        state[(12-i)%14] = 0

    elif(player == 0 and state[i%14] == 1 and state[(12-i)%14] != 0 and i%14 > 6 and i%14 < 13 and stealing):
        state[13] += state[i%14]
        state[13] += state[(12-i)%14]
        state[i%14] = 0
        state[(12-i)%14] = 0

    if(state[0] == 0 and state[1] == 0 and state[2] == 0 and state[3] == 0 and state[4] == 0 and state[5] == 0 ):
        state[13] = state[13] + state[7] + state[8] + state[9] + state[10] + state[11] + state[12]
        state[7] = 0
        state[8] = 0
        state[9] = 0
        state[10] = 0
        state[11] = 0
        state[12] = 0



    if(state[7] == 0 and state[8] == 0 and state[9] == 0 and state[10] == 0 and state[11] == 0 and state[12] == 0 ):
        state[6] = state[6] + state[0] + state[1] + state[2] + state[3] + state[4] + state[5]
        state[0] = 0
        state[1] = 0
        state[2] = 0
        state[3] = 0
        state[4] = 0
        state[5] = 0

    if(player == 1 and i%14 != 6 and not(test_mode)):
        playerturn =  int(not(playerturn))
    if(player == 0 and i%14 != 13 and not(test_mode)):
        playerturn =  int(not(playerturn))
    if(player == 1 and i%14 != 6 and test_mode):
        ai_turn =  int(not(ai_turn))
    if(player == 0 and i%14 != 13 and test_mode):
        ai_turn =  int(not(ai_turn))



def show_game(state): 
    print("|----0--1--2--3--4--5----|")
    print("|[{}]({})({})({})({})({})({})[ ]|".format(state[13],state[12],state[11],state[10],state[9],state[8],state[7]))
    print("|[ ]({})({})({})({})({})({})[{}]|".format(state[0],state[1],state[2],state[3],state[4],state[5],state[6]))
    print("|----0--1--2--3--4--5----|")
    print("++++++++++++++++++++++++++")

def game(player1,player2,diffculty=6): 
    state = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
    game_not_finished = True
    quit = False
    show_game(state)
    while(game_not_finished):
        if(playerturn):
            if(player1 == 1): #ai player
                move = Maxmin(state,diffculty,0)
                makemove(state,move,1,0)
            if(player1 == 0): #human player
                move = player_move(state,1)
                if(move == 13):
                    quit = True
                    break;
                makemove(state,move,1,0)
        else:
            if(player2 == 1): #ai player
                move = Maxmin(state,diffculty,0)
                makemove(state,move,0,0)
            if(player2 == 0): #human player
                move = player_move(state,2)
                if(move == 13):
                    quit = True
                    break;
                makemove(state,move,0,0)
        show_game(state)
        game_not_finished = end_game(state)
    if(quit):
        return
    winning_message(state)


easy = 2
medium = 6
hard = 10

while(True):
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
                game(0,1,easy)
                break
            elif( userinput == "2"):
                print("\nai is on medium difficulty\n")
                game(0,1,medium)
                break
            elif( userinput == "3"):
                print("\nai is on hard difficulty\n")
                game(0,1,hard)
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

