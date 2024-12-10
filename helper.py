import re
from collections import *
import heapq


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


class Grid:
	def __init__(self, x, cell_type=None):
		if not cell_type: cell_type = type(x[0][0])
		self.grid = [[cell_type(a) for a in list(line)] for line in x]
		self.height = len(self.grid)
		self.width = len(self.grid[0])
		self.h = self.height
		self.w = self.width
		self.area = self.height * self.width


	def __getitem__(self, x):
		return self.grid[x]


	def __iter__(self):
		for r in range(self.height):
			for c in range(self.width):
				yield self.grid[r][c]


	def __str__(self):
		return '\n'.join([''.join(map(str,line)) for line in self.grid])


	def get_neighbour_coords(self, point, diag=False):
		(r, c) = point
		neighbour_cells = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

		if diag:
			neighbour_cells.extend([(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)])

		n = []
		for (r, c) in neighbour_cells:
			if self.valid(r, c):
				n.append((r, c))

		return n


	def get_neighbours(self, point, diag=False):
		cells = []
		for (r, c) in self.get_neighbour_coords(point, diag):
			cells.append(self.grid[r][c])

		return cells


	def subgrid(self, x1, y1, x2, y2):
		return [row[y1:y2+1] for row in self.grid[x1:x2+1]]


	def cells_in_subgrid(self, x1, y1, x2, y2):
		for r in range(x1, x2+1):
			for c in range(y1, y2+1):
				yield self.grid[r][c]


	def all_points(self):
		for r in range(self.height):
			for c in range(self.width):
				yield (r, c)


	def count(self, symbol):
		return sum([line.count(symbol) for line in self.grid])


	def valid(self, r, c):
		return (0 <= r < self.height) and (0 <= c < self.width)


	def get(self, point):
		(r, c) = point
		return self.grid[r][c]


	def set(self, point, symbol):
		(r, c) = point
		self.grid[r][c] = symbol


	def find(self, symbol):
		return [(r, c) for (r, c) in self.all_points() if self.grid[r][c] == symbol]


	def transpose(self):
		self.grid = list(map(list, zip(*self.grid)))
		self.height = len(self.grid)
		self.width = len(self.grid[0])


	def rotate_90(self):
		self.grid = self.grid[::-1]
		self.transpose()


def triangle(n):
	return n * (n + 1) // 2


def add_tuples(a, b):
	return tuple( [a[i] + b[i] for i in range(len(a))] )


def sub_tuples(a, b):
	return tuple( [a[i] - b[i] for i in range(len(a))] )


def mul_tuples(a, b):
	return tuple( [a[i] * b[i] for i in range(len(a))] )


def shoelace_formula(coords):
	n = len(coords)
	area = 0

	for i in range(n):
		j = (i + 1) % n
		area += coords[i][0] * coords[j][1]
		area -= coords[j][0] * coords[i][1]

	return abs(area) // 2


def picks_theorem(inner_points, border_points):
	"""
	Find area of shape using
		A = I + B/2 - 1
	"""
	return inner_points + (border_points / 2) - 1


def manhattan_dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def BFS(grid, start):
	seen = set()
	q = deque([start])

	while q:
		node = q.popleft()
		if node not in seen:
			seen.add(node)
			q.extend([n for n in grid.get_neighbour_coords(node) if n not in seen])

	return seen


def DFS(grid, start):
	seen = set()
	q = [start]

	while q:
		node = q.pop()
		if node not in seen:
			seen.add(node)
			q.extend([n for n in grid.get_neighbour_coords(node) if n not in seen])

	return seen


def floyd_warshall(nV, grid):
	"""
	nV = number of verticies
	"""
	distance = list(map(  lambda i: list(map(lambda j: j, i)), grid  ))

	for k in range(nV):
		for i in range(nV):
			for j in range(nV):
				distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
	return distance


def dijkstra(grid, start, goal):
	distances = {node: float('infinity') for node in grid.all_points()}
	distances[start] = 0

	pq = [(0, start)]

	while pq:
		curr_dist, curr_node = heapq.heappop(pq)

		if curr_node == goal:
			return curr_dist

		if curr_dist > distances[curr_node]:
			continue

		for n in grid.get_neighbours(curr_node):
			dist = curr_dist + grid.get(n)

			if dist < distances[n]:
				distances[n] = dist
				heapq.heappush(pq, (dist, n))

	return -1

	
acc_2d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
acc_3d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

#move = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
#turn = {'^': '>', 'v':'<', '>':'v', '<': '^'}


def ints(x, neg=True):
	if neg:
		return [int(num) for num in re.findall("[-\d]+", x)]
	else:
		return [int(num) for num in re.findall("[\d]+", x)]

def digits(x, neg=False):
	if neg:
		return [int(num) for num in re.findall("-?\d", x)]
	else:
		return [int(num) for num in re.findall("\d", x)]
