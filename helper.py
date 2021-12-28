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


def triangle(n):
	return n * (n + 1) // 2


def ints(x):
	return [int(num) for num in re.findall("[-\d]+", x)]