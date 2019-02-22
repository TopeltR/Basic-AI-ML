
from prax3.NQPosition import NQPosition

# panna nad ühte masiivi, mis on veergude masiiv, saab optimeerida O(n) peale O(N ruut)
# peale ühe ümber tõstmist arvutada naaberolekute arv
def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value >= curr_value:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


pos = NQPosition(4) # test with the tiny 4x4 board first
print(pos.get_board())
print("Initial position value", pos.value())
#best_pos, best_value = hill_climbing(pos)
#print("Final value", best_value)
# if best_value is 0, we solved the problem