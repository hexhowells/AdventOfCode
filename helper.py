import re


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


	def __getitem__(self, x):
		return self.grid[x]


	def __iter__(self):
		for r in range(self.height):
			for c in range(self.width):
				yield self.grid[r][c]


	def __str__(self):
		return '\n'.join([''.join(line) for line in self.grid])


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


def triangle(n):
	return n * (n + 1) // 2


def add_tuples(a, b):
	return tuple( [a[i] + b[i] for i in range(len(a))] )


def sub_tuples(a, b):
	return tuple( [a[i] - b[i] for i in range(len(a))] )


def mul_tuples(a, b):
	return tuple( [a[i] * b[i] for i in range(len(a))] )

	
acc_2d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
acc_3d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def ints(x):
	return [int(num) for num in re.findall("[-\d]+", x)]


def digits(x, neg=False):
	if neg:
		return [int(num) for num in re.findall("-?\d", x)]
	else:
		return [int(num) for num in re.findall("\d", x)]
