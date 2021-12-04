from collections import *
import math
import numpy as np


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()
	return data.rstrip()


def parse_data(x):
	nums = [int(num) for num in x[0].split(',')]
	grids = np.zeros((5, 5, 2, len(x[1:])))

	for g, grid in enumerate(x[1:]):
		for r, row in enumerate(grid.split('\n')):
			for c, col in enumerate(row.split()):
				grids[r, c, 0, g] = int(col)

	return nums, grids, len(x[1:])


def bingo(grid_2d):
	for i in range(5):
		if sum(grid_2d[i,:]) == 5 or sum(grid_2d[:,i]) == 5:
			return True
	return False


def score(grid):
	return np.sum(np.where(grid[:,:,1]==0, grid[:,:,0], 0))


def solutions(x):
	part1 = part2 = None
	nums, grids, grid_count = parse_data(x)

	grid_wins = [0] * grid_count
	for num in nums:
		for i in range(grid_count):
			if grid_wins[i] == 1: continue

			if num in grids[:,:,0,i]:
				r, c = np.where(grids[:,:,0,i]==num)
				grids[r, c, 1, i] = 1

				if bingo(grids[:,:,1,i]):
					if sum(grid_wins) == 0:
						part1 = int(score(grids[:,:,:,i]) * num)

					grid_wins[i] = 1
					if sum(grid_wins) == grid_count:
						part2 = int(score(grids[:,:,:,i]) * num)

	return part1, part2


data = collect_input("input.txt")
data = [x for x in data.split('\n\n')]

part1, part2 = solutions(data)
print("{}\n{}".format(part1, part2))