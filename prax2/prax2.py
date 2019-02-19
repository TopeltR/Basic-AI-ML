from queue import Queue, PriorityQueue

lava_map1 = [
	"      **               **      ",
	"     ***     D        ***      ",
	"     ***                       ",
	"                      *****    ",
	"           ****      ********  ",
	"           ***          *******",
	" **                      ******",
	"*****             ****     *** ",
	"*****              **          ",
	"***                            ",
	"              **         ******",
	"**            ***       *******",
	"***                      ***** ",
	"                               ",
	"                s              ",
]

lava_map2 = [
	"     **********************    ",
	"   *******   D    **********   ",
	"   *******                     ",
	" ****************    **********",
	"***********          ********  ",
	"            *******************",
	" ********    ******************",
	"********                   ****",
	"*****       ************       ",
	"***               *********    ",
	"*      ******      ************",
	"*****************       *******",
	"***      ****            ***** ",
	"                               ",
	"                s              ",
]
start_row = 2
start_col = 2
start = (start_col, start_row)
goal = (257, 295)


def read_map(lava_map):
	with open(lava_map) as f:
		map_data = [l.strip() for l in f.readlines() if len(l) > 1]
	return map_data


def not_outside_map(neighbour, height, width):
	return height > neighbour[1] >= 0 and width > neighbour[0] >= 0


def is_not_lava(lava_map, neighbour):
	return lava_map[neighbour[1]][neighbour[0]] is not "*"


def draw_path(lava_map: list, path: list) -> None:
	for coord in path[:-1]:
		lava_map[coord[1]][coord[0]] = "."
	print("\n".join(["".join(row) for row in lava_map]))


def get_neighbours(location: tuple, lava_map: list) -> list:
	x = location[0]
	y = location[1]
	neighbours = []
	for y_neighbour in [-1, 0, 1]:
		for x_neighbour in [-1, 0, 1]:
			neighbour = (x + x_neighbour, y + y_neighbour)
			if abs(y_neighbour) + abs(x_neighbour) == 1:
				if not_outside_map(neighbour, len(lava_map), len(lava_map[0])):
					if is_not_lava(lava_map, neighbour):
						neighbours.append(neighbour)
	return neighbours


def minu_otsing(map, start):
	map = [list(row) for row in map]
	frontier = Queue()
	frontier.put(start)
	came_from = {start: None}
	while not frontier.empty():
		current = frontier.get()
		if map[current[1]][current[0]] == 'D':
			break
		for next in get_neighbours(current, map):
			if next not in came_from:
				frontier.put(next)
				came_from[next] = current
	path = []
	while came_from[current] is not None:
		path.append(current)
		current = came_from[current]

	path.reverse()

	draw_path(map, path)
	return path


def h(next, goal):
	return abs(next[0] - goal[0]) + abs(next[1] - goal[1])


def greedy(lava_map, start, goal):
	card = read_map(lava_map)
	map = [list(row) for row in card]
	print(map)
	frontier = PriorityQueue()
	frontier.put((0, start))
	came_from = {start: None}
	while not frontier.empty():
		current = frontier.get()
		#print(current)
		#print(map[current[1][1]][current[1][0]])
		if map[current[1][1]][current[1][0]] == 'D':
			break
		for next in get_neighbours(current[1], map):
			if next not in came_from:
				priority = h(next, goal)
				frontier.put((priority, next))
				came_from[next] = current
	path = []
	while came_from[current] is not None:
		path.append(current)
		current = came_from[current]

	path.reverse()

	draw_path(map, path)
	return path


#minu_otsing(lava_map2, start)
greedy("cave300x300", start, goal)
