def ball_game(arr,max_turn):
    turn = 0
    child_pick = 0
    while turn < max_turn:
        try:
            child_pick = arr[child_pick]
        except IndexError:
            break
        turn += 1
    return child_pick
print(ball_game([1, 3, 2], 1))
print(ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 5))
print(ball_game([8, 7, 1, 5, 3, 10, 4, 2, 6, 9], 7))