from collections import *
import math
from timeit import default_timer as timer
import itertools


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_grid(x):
	return [list(line) for line in x]


def part1(x):
	grid = get_grid(x)
	h = len(grid)
	w = len(grid[0])

	for step in range(1000):
		has_moved = False

		# Move East
		for i in range(h):
			new_line = grid[i].copy()
			for j in range(w):
				j_next = (j + 1) % w
				if grid[i][j] == ">" and grid[i][j_next] == ".":
					has_moved = True
					new_line[j_next] = grid[i][j]
					new_line[j] = '.'
			grid[i] = new_line

		# Move South
		new_grid = [[grid[i][j] for j in range(w)] for i in range(h)]
		for i in range(h):
			i_next = (i + 1) % h
			for j in range(w):
				if grid[i][j] == "v" and grid[i_next][j] == ".":
					has_moved = True
					new_grid[i_next][j] = grid[i][j]
					new_grid[i][j] = '.'
		grid = new_grid
		
		if not has_moved:
			return step+1
	
	return -1


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(part1(data))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))