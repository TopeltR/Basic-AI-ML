class NQPosition:
	def __init__(self, N):
		# choose some internal representation of the NxN board
		# put queens on it
		global board
		global rows
		board = [["." for i in range(N)] for j in range(N)]
		rows = [0 for i in range(N)]
		self.place_queens()

	def value(self):
		# calculate number of conflicts (queens that can capture each other)
		# return value
		pass

	def make_move(self, move):
		# get the position from tuple
		i = move[0]
		j = move[1]
		# change the value on board
		board[i][j] = "*"

	# remove old value

	def best_move(self):
		# kaks fori, lipud ja rida, kontrollid seda sama ühedim masiivi, et ei ole sama rida
		# best-value, best-lipp- best-rida
		# oleks[lipp] = rida ja value = f(olek)
		for queen in range(len(board)):
			for row in range(len(rows)):
				pass
		pass

	# find the best move and the value function after making that move
	# return move, value

	# *
	# 3 * 1
	# 2 4 *
	#       *
	def free_row(self, row) -> bool:
		for i in range(len(board)):
			if board[i][row] == "*":
				return False
		return True

	def free_col(self, col) -> bool:
		for j in range(len(board)):
				if board[col][j] == "*":
					return False
		return True

	def place_queens(self):
		for i in range(len(board)):
			for j in range(len(board)):
				if self.free_col(i):
					if self.free_row(j):
						board[i][j] = "*"
						rows[i] = i
		print(rows)

	def get_board(self):
		print("\n".join(["".join(row) for row in board]))
