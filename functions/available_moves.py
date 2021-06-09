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
