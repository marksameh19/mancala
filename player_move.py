def player_move(moves,player): 
    userInput = " "
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
