from game import makemove
import global_settings
import available_moves
import makemove

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