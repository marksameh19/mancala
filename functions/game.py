import global_settings
from show_game import show_game
from make_move import makemove
from player_move import player_move
from end_game import end_game
from winning_message import winning_message
from maxmin import Maxmin

def game(player1,player2,diffculty=6):
    state = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
    game_not_finished = True
    quit = False
    show_game(state)
    while(game_not_finished):
        if(global_settings.playerturn):
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

