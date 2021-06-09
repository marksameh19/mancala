def end_game(moves):
    sideOne = 0
    sideTwo = 0
    for j in range(6):
        sideOne = int(sideOne) + int(moves[j])
        sideTwo = int(sideTwo) + int(moves[j+7])

    if int(sideOne) == 0 or int(sideTwo) == 0:
        return False
    else:
        return True
