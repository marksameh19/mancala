import get_children
import end_game
import global_settings


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