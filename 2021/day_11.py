from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_neighbours(grid, point):
	height, width = len(grid), len(grid[0])
	(r, c) = point
	neighbour_cells = [(r-1, c), (r+1, c), (r, c-1), (r, c+1), 
				(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]

	n = []
	for (r, c) in neighbour_cells:
		if (0 <= r < height) and (0 <= c < width):
			n.append((r, c))

	return n


def all_points(grid):
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			yield (r, c)


def update_energy(grid, flashes, r, c):
	if grid[r][c] == 9:
		flashes.append((r,c))
		grid[r][c] = 0
	else:
		grid[r][c] += 1


def solutions(x):
	grid = [[int(cell) for cell in line] for line in x]
	part1 = part2 = 0

	for day in range(1000):
		if sum([sum(row) for row in grid]) == 0:
			part2 = day
			break

		flashes = []
		for (r, c) in all_points(grid):
			update_energy(grid, flashes, r, c)

		while flashes:
			if day < 100: part1 += 1

			(rr, cc) = flashes.pop()
			for (rn, cn) in get_neighbours(grid, (rr,cc)):
				if grid[rn][cn] != 0:
					update_energy(grid, flashes, rn, cn)
	
	return part1, part2


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

part1, part2 = solutions(data)
print("{}\n{}".format(part1, part2))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))