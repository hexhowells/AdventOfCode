from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def parse_data(x):
	a, b = x
	coords = [[int(x) for x in y.split(',')] for y in a.split("\n")]
	Folds = namedtuple("Folds", "axis pos")
	folds = []
	for line in b.split("\n"):
		axis, num = line.split("=")
		folds.append(Folds(axis[-1], int(num)))

	return coords, folds


get_size = lambda c, i: max([x[i] for x in c]) + 1

def create_grid(coords):
	h = get_size(coords, 1)
	w = get_size(coords, 0)
	grid = np.zeros((h, w))

	for (r, c) in coords:
		grid[c][r] = 1

	return grid


def solutions(x):
	part1 = 0

	coords, folds = parse_data(x)
	grid = create_grid(coords)
	
	for i, fold in enumerate(folds):
		if fold.axis == "y":
			a = grid[:fold.pos, :]
			b = np.flip(grid[fold.pos+1:, :], 0)
		else:
			a = grid[:, :fold.pos]
			b = np.flip(grid[:, fold.pos+1:], 1)

		grid = np.add(a, b)
		if i == 0: part1 = np.count_nonzero(grid >= 1)
	
	code = [["#" if v >= 1 else " " for v in row] for row in grid]
	
	return part1, code


data = collect_input("input.txt")
data = [x for x in data.split('\n\n')]

start = timer()

part1, part2 = solutions(data)
print(part1)
[print(''.join(line)) for line in part2]

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))