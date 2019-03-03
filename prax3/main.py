import random


class NQPosition:
	def __init__(self, N):
		# choose some internal representation of the NxN board
		# put queens on it
		self.board = [random.randrange(N) for _ in range(N)]
		self.n = N

	def value(self):
		value = 0
		for col1, queen1 in enumerate(self.board):
			for col2 in range(col1 + 1, self.n):
				queen2 = self.board[col2]
				# check row
				if queen1 == queen2:
					value += 1
				# Check diag
				if abs(queen2 - queen1) == abs(col2 - col1):
					value += 1
		return value

	def make_move(self, queen_idx, row):
		self.board[queen_idx] = row

	def best_move(self):
		# find the best move and the value function after making that move
		move = ()
		value = self.value()
		for i in range(self.n):
			queen_idx = i
			prev_row = self.board[queen_idx]
			for queen_row in range(self.n):
				if queen_row != prev_row:
					self.make_move(queen_idx, queen_row)
					new_value = self.value()
					if new_value < value:
						value = new_value
						move = (queen_idx, queen_row)
					self.make_move(queen_idx, prev_row)
		return move, value

	def print_board(self) -> None:
		board = []
		for row in range(self.n):
			board_row = []
			for q in self.board:
				board_row.append(str(1) + " " if q == row else str(0) + " ")
			board.append(board_row)

		print('\n'.join([''.join(row) for row in board]))
		print()


def hill_climbing(pos):
	curr_value = pos.value()
	while True:
		# pos.print_board()
		move, new_value = pos.best_move()
		if new_value >= curr_value:
			# no improvement, give up
			return pos, curr_value
		else:
			# position improves, keep searching
			curr_value = new_value
			pos.make_move(move[0], move[1])


def random_restart_hillclimbing(n):
	final_value = n
	restart_nr = 0
	best_pos = None
	while final_value != 0:
		pos = NQPosition(n)
		best_pos, final_value = hill_climbing(pos)
		restart_nr += 1
		if restart_nr == 100:
			print("Could not find solution")
			return
	print(f"Restart nr: {restart_nr}")
	best_pos.print_board()
	print("Final value", final_value)


random_restart_hillclimbing(100)
