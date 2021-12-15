from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import heapq


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_neighbours(grid, point):
	height, width = len(grid), len(grid[0])
	(r, c) = point
	neighbour_cells = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

	n = []
	for (r, c) in neighbour_cells:
		if (0 <= r < height) and (0 <= c < width):
			n.append((r, c))

	return n


def all_points(h, w):
	for r in range(h):
		for c in range(w):
			yield (r, c)


def create_grid(x):
	return [[int(a) for a in list(line)] for line in x]


def expand(grids, n):
	for i in range(n-1):
		new = grids[-1] + 1
		new = np.where(new <= 9, new, 1)
		grids.append(new)
	return grids


def expand_grid(grid, n):
	if n == 1: return grid

	grid = np.asarray(grid)

	cols = expand([grid], n)
	grid = np.hstack(cols)

	rows = expand([grid], n)
	grid = np.vstack(rows)

	return np.ndarray.tolist(grid)


def solutions(x, n):
	grid = create_grid(x)
	grid = expand_grid(grid, n)
	h = len(grid)
	w = len(grid[0])

	start_pos = (0, 0)
	pq = [(0, start_pos)]
	
	distances = {}
	for p in all_points(h, w):
		distances[p] = float("inf")
	distances[start_pos] = 0

	while pq:
		cur_dist, cur_pos = heapq.heappop(pq)

		for (r, c) in get_neighbours(grid, cur_pos):
			dist = cur_dist + grid[r][c]

			if dist < distances[(r, c)]:
				distances[(r, c)] = dist
				heapq.heappush(pq, (dist, (r,c)))

	return (distances[(h-1, w-1)])


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(solutions(data, 1))

# Part 2
print(solutions(data, 5))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))