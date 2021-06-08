def game(player1,player2,diffculty=6): #samuel
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
        print("\ntoo coward to challenge our ai?\n")
        return
    winning_message(state)

