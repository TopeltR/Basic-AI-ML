import random
from collections import defaultdict

DUMMY_AI = 0
MINIMAX_AI = 1

ROLL = 0
PASS = 1


def pig_game(ai_func, ai_func2):
    rolled = 0
    turn = MINIMAX_AI
    dummy_ai_points = minimax_ai_points = 0

    while dummy_ai_points < 100 and minimax_ai_points < 100:
        if turn == MINIMAX_AI:
            decision = ai_func(turn, rolled, dummy_ai_points, minimax_ai_points)

            if decision == PASS:
                rolled = 0
                turn = DUMMY_AI
            else:
                dieroll = random.randint(1, 6)
                # print("You rolled...", dieroll)
                if dieroll == 1:
                    minimax_ai_points -= rolled  # lose all points again
                    rolled = 0
                    turn = DUMMY_AI
                else:
                    rolled += dieroll
                    minimax_ai_points += dieroll

        else:
            decision = ai_func2(turn, rolled, dummy_ai_points, minimax_ai_points)
            if decision == PASS:
                #  print("-- AI decides to pass.")
                rolled = 0
                turn = MINIMAX_AI
            else:
                dieroll = random.randint(1, 6)
                #  print("-- AI rolled...", dieroll)
                if dieroll == 1:
                    dummy_ai_points -= rolled  # lose all points again
                    rolled = 0
                    turn = MINIMAX_AI
                else:
                    rolled += dieroll
                    dummy_ai_points += dieroll

    if minimax_ai_points >= 100:
        return 1
    elif dummy_ai_points >= 100:
        return 2


def dummy_ai(turn, rolled, my_points, opp_points):
    if rolled < 21:
        return ROLL
    else:
        return PASS


def minimax_ai(turn, rolled, my_points, opp_points):
    # this is the top level of search
    # we search all possible moves
    # (PASS and ROLL in case of the Pig game)
    # and pick the one that returns the highest minimax estimate
    depth = 5
    pass_val = exp_minimax(DUMMY_AI, False, PASS, 0, opp_points, depth)
    roll_val = exp_minimax(MINIMAX_AI, True, ROLL, my_points, opp_points, depth)
    best_val = max(pass_val, roll_val)

    if best_val == pass_val:
        exp_minimax(MINIMAX_AI, True, PASS, my_points, opp_points, depth)
    else:
        exp_minimax(MINIMAX_AI, True, ROLL, my_points, opp_points, depth)


def exp_minimax(turn, chance, rolled, my_points, opp_points, depth):
    # update remaining depth as we go deeper in the search tree
    depth -= 1

    # case 1a: somebody won, stop searching
    # return a high value if AI wins, low if it loses.
    if my_points > 100 and opp_points < 100:
        return 1000
    elif opp_points > 100 and my_points < 100:
        return -1000
    # case 1b: out of depth, stop searching
    # return game state eval (should be between win and loss)
    if depth <= 0:
        if turn == DUMMY_AI:
            return opp_points
        else:
            return my_points

    # case 2: AI's turn (and NOT a chance node):
    # return max value of possible moves (recursively)
    if turn == DUMMY_AI and not chance:
        return max(exp_minimax(MINIMAX_AI, False, 0, my_points, opp_points, depth),
                   exp_minimax(DUMMY_AI, True, rolled, my_points, opp_points, depth))
    # case 3: player's turn:
    # return min value (assume optimal action from player)
    if turn == MINIMAX_AI and not chance:
        return min(exp_minimax(DUMMY_AI, False, 0, my_points, opp_points, depth),
                   exp_minimax(MINIMAX_AI, True, rolled, my_points, opp_points, depth))

    # case 4: chance node:
    # return average of all dice rolls
    if turn == MINIMAX_AI and chance:
        average = 0
        for i in range(1, 6):
            if i == 1:  # border case
                average += exp_minimax(DUMMY_AI, False, 0, my_points - rolled, opp_points, depth)  # lost points
            else:
                average += exp_minimax(MINIMAX_AI, False, rolled, my_points + rolled, opp_points, depth)  # gain points
        return average / 6

    if turn == DUMMY_AI and chance:
        average = 0
        for i in range(1, 6):
            if i == 1:
                average += exp_minimax(DUMMY_AI, False, 0, my_points, opp_points - rolled, depth)
            else:
                average += exp_minimax(MINIMAX_AI, False, rolled, my_points, opp_points + rolled, depth)
        return average / 6


if __name__ == '__main__':
    stats = defaultdict(int)
    for _ in range(10):
        for _ in range(100):
            winner = pig_game(dummy_ai, minimax_ai)
            stats[winner] += 1
    print('Expectiminimax AI winning percentage {} %'.format(stats[1] / 10))
    print('Dummy AI winning percentage {} %'.format(stats[2] / 10))

