import numpy as np


def math_game():
    operators = ['+', '-', '*', '/']
    numbers = list(range(-100, 100))
    exist_flag = False

    score = 0
    while exist_flag is False:
        operator = np.random.choice(operators)
        question = '{} {} {}'.format(np.random.choice(numbers),
                                     operator,
                                     np.random.choice(numbers))
        try:
            result = eval(question)
        except ZeroDivisionError:
            question = '{} {} {}'.format(np.random.choice(numbers),
                                         operator,
                                         np.random.choice(numbers))
            result = eval(question)

        answer = eval(input(question+' = '))
        while abs(answer-result) >= 0.1:
            print("You are wrong! Try again")
            answer = input(question+' =')
        if abs(answer-result) <= 0.1:
            print('You are right! Plus 5 points')
            score += 5

        print("Your score is: "+str(score))
        if input("Press return to continue") == '':
            continue
        else:
            exist_flag == True
        

# 17M_5 is in the xlsx
"""
def board_game():
    size = 4
    osize = size-1
    board = np.array(list(range(1, size**2+1))).reshape((size, size))
    board[osize, osize] = 'Home'
    A = [0, 0]
    B = [1, 1]

    vertical_move = lambda x, y, x2: True if x[0] < osize and y[0] != x[0] and x[0] and x[0]-x2[0] == 1 else False
    horizontal_move = lambda x, y, x2: True if x[1] < osize and y[1] != x[1] x[1]-x2[1] == 1 else False
    diagonal_move = lambda x, y, x2: True if x[1] < osize and x[0] < osize and y[0] != x[0] and y[1] != x[1] else False

    move_test = lambda x, y, x2: True if vertical_move(x, y) and horizontal_move(x, y) and diagonal_move(x, y) else False
    success = lambda x, y: True if (x[1] == osize and x[0] == osize) or (y[1] == osize and y[0] == osize) else False

    print("Type in 'A to 3' to move A")
    while success(A, B) is False:
        A_move = input("Your move: ")
        target = eval(A_move.split(' ')[-1])

        target_position = np.where(board == target)[0][0], np.where(board == target)[1][0]

        # validate A move and operate move
        if move_test(target_position, B, A):
            A = target_position
        else:
            print("Can't make that move, change one.")
            continue

        # A moved, now find where B can go
        def nbility(A, B):
            B_targets = []
            
            B_target = [B[0] + 1, B[1]]
            B_targets.append(B_target) if vertical_move(B_target, A, B)

            B_target = [B[0], B[1] + 1]
            B_targets.append(B_target) if horizontal_move(B_target, A, B)

            B_target = [B[0]+1, B[1]+1]
            B_targets.append(B_target) if diagonal_move(B_target, A, B)
"""
        




    
