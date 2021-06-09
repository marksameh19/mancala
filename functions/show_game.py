def show_game(state): 
    print("|----0--1--2--3--4--5----|")
    print("|[{}]({})({})({})({})({})({})[ ]|".format(state[13],state[12],state[11],state[10],state[9],state[8],state[7]))
    print("|[ ]({})({})({})({})({})({})[{}]|".format(state[0],state[1],state[2],state[3],state[4],state[5],state[6]))
    print("|----0--1--2--3--4--5----|")
    print("++++++++++++++++++++++++++")