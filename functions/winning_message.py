def winning_message(moves):
    print("")
    print("The game is over!")
    if int(moves[13]) < int(moves[6]):
        print("Player One has won the game!")
    elif int(moves[13]) > int(moves[6]):
        print("Player Two has won the game!")
    else:
        print("The game ended in a tie.")
