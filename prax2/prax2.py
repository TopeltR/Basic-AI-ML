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
goal = (598, 595)

start = (2, 2)
goal_300 = (295, 257)
goal_600 = (598, 595)
goal_900 = (898, 895)


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
		lava_map[coord[1][1]][coord[1][0]] = "."
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


def h(next, goal):
	return abs(next[1] - goal[1]) + abs(next[0] - goal[0])


def greedy(lava_map, start, goal):
	card = read_map(lava_map)
	map = [list(row) for row in card]
	frontier = PriorityQueue()
	frontier.put((0, start))
	came_from = {start: None}
	while not frontier.empty():
		_, current = frontier.get()
		if map[current[1]][current[0]] == 'D':
			break
		for next in get_neighbours(current, map):
			if next not in came_from:
				priority = h(next, goal)
				frontier.put((priority, next))
				came_from[next] = current
	path = []
	while came_from[current] is not None:
		path.append(current)
		current = came_from[current]

	path.reverse()
	print(len(path))
	return path


def astar(lava_map, start, goal):
	card = read_map(lava_map)
	map = [list(row) for row in card]
	frontier = PriorityQueue()
	frontier.put((0, start))
	came_from = {start: None}

	cost_so_far = {}
	cost_so_far[start] = 0

	while not frontier.empty():
		_, current = frontier.get()
		if map[current[1]][current[0]] == 'D':
			break
		for next in get_neighbours(current, map):
			new_cost = cost_so_far[current] + 1
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + h(next, goal)  # g(n) + h(n)
				frontier.put((priority, next))
				came_from[next] = current
	path = []
	while came_from[current] is not None:
		path.append(current)
		current = came_from[current]

	path.reverse()
	print(len(path))
	return path


# minu_otsing(lava_map2, start)
greedy("cave300x300", start, goal_300)
astar("cave300x300", start, goal_300)
print("\n")
greedy("cave600x600", start, goal_600)
astar("cave600x600", start, goal_600)
print("\n")
greedy("cave900x900", start, goal_900)
astar("cave900x900", start, goal_900)
