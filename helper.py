import re


def get_neighbours(grid, point, diag=False):
	height, width = len(grid), len(grid[0])
	(r, c) = point
	neighbour_cells = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

	if diag:
		neighbour_cells.append([(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)])

	n = []
	for (r, c) in neighbour_cells:
		if (0 <= r < height) and (0 <= c < width):
			n.append((r, c))

	return n


def all_points(grid):
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			yield (r, c)


def create_grid(x):
	return [[int(a) for a in list(line)] for line in x]


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
			if (0 <= r < self.height) and (0 <= c < self.width):
				n.append((r, c))

		return n


	def get_neighbours(self, point, diag=False):
		cells = []
		for (r, c) in self.get_neighbour_coords(point, diag):
			cells.append(self.grid[r][c])

		return cells


	def all_points(self):
		for r in range(self.height):
			for c in range(self.width):
				yield (r, c)


	def count(self, symbol):
		return sum([line.count(symbol) for line in self.grid])


	def valid(self, r, c):
		return (0 <= r < self.height) and (0 <= c < self.width)



def triangle(n):
	return n * (n + 1) // 2


def ints(x):
	return [int(num) for num in re.findall("[-\d]+", x)]