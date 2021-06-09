def makemove(state,move,player,test_mode): #hazem
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
