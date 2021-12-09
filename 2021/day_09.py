from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_neighbours(grid, point):
	h, w = len(grid), len(grid[0])
	(r, c) = point

	n = []
	if r-1 >= 0: n.append((r-1, c))
	if r+1 < h: n.append((r+1, c))
	if c-1 >= 0: n.append((r, c-1))
	if c+1 <w: n.append((r, c+1))

	return n


def all_points(grid):
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			yield (r, c)


def part1(x):
	grid = []

	for line in x:
		grid.append([int(v) for v in line])

	acc = 0
	for r, c in all_points(grid):
		p = grid[r][c]
		n = get_neighbours(grid, (r,c))

		if sum([p < grid[r][c] for r,c in n]) == len(n):
			acc += (1+int(p))
	return acc


# Flood Fill Algorithm
def part2(x):
	grid = []

	for line in x:
		grid.append([int(v) for v in line])

	acc = 0
	seen = set()
	basin_sizes = []

	for r, c in all_points(grid):
		if (r,c) not in seen and grid[r][c] != 9:
			q = deque()
			q.append((r,c))
			size = 0

			while q:
				p = q.popleft()
				if p in seen: continue
				seen.add(p)
				size += 1

				for n in get_neighbours(grid, p):
					(r, c) = n
					if grid[r][c] != 9:
						q.append(n)

			basin_sizes.append(size)

	basin_sizes.sort()
	return math.prod([s for s in basin_sizes[-3:]])



data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))