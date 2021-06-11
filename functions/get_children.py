from make_move import makemove
from available_moves import available_moves
import global_settings


def get_children(state,player): 
    constant_turn = global_settings.ai_turn
    children = []
    for move in available_moves(state,player):
        new_state = state[:]
        makemove(new_state,move,player,1)
        children.append([new_state,move,global_settings.ai_turn])
        global_settings.ai_turn = constant_turn
    return children