from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_neighbours(elf, elfs):
	pos = {'N':(-1, 0), 'E':(0, 1), 'S':(1, 0), 'W':(0, -1),
			'NE': (-1, 1), 'SE':(1, 1), 'SW':(1, -1), 'NW':(-1, -1)}

	elf_d = []
	for d, acc in pos.items():
		if (elf[0]+acc[0], elf[1]+acc[1]) in elfs:
			elf_d.append(d)

	return elf_d


check_direcs = [
		['N', 'NE', 'NW', (-1, 0)],
		['S', 'SE', 'SW', (1, 0)],
		['W', 'NW', 'SW', (0, -1)],
		['E', 'NE', 'SE', (0, 1)]]

def get_move_direction(d):
	move = (0, 0)
	for chk1, chk2, chk3, acc in check_direcs:
		if (chk1 not in d) and (chk2 not in d) and (chk3 not in d):
			return acc

	return move


def get_area(elfs):
	minr, maxr, minc, maxc = 1_000_000, -1_000_000, 1_000_000, -1_000_000
	for elf in elfs:
		minr = min(minr, elf[0])
		maxr = max(maxr, elf[0])
		minc = min(minc, elf[1])
		maxc = max(maxc, elf[1])

	return (maxr - minr+1) * (maxc - minc+1)


def solve(x):
	grid = aoc.Grid(x)
	elfs = []
	part1 = None

	# get the initial locations of all the elfs
	for (r, c) in grid.all_points():
		if grid[r][c] == '#': elfs.append((r, c))

	for epoch in range(100_000):
		new_elfs = []
		prop_elfs = {}
		elfs_set = set(elfs)

		# get next elf positions
		for elf in elfs:
			neighbours = get_neighbours(elf, elfs_set)

			if len(neighbours) == 0:
				new_pos = elf
			else:
				direc = get_move_direction(neighbours)
				new_pos = (elf[0]+direc[0], elf[1]+direc[1])

			if new_pos not in prop_elfs:
				prop_elfs[new_pos] = [elf]
			else:
				prop_elfs[new_pos].append(elf)
				
		# try to move the elfs
		for k, v in prop_elfs.items():
			if len(prop_elfs[k]) == 1:
				new_elfs.append(k)
				elf_moved = True
			else:
				for old in v:
					new_elfs.append(old)

		if elfs_set == set(new_elfs): return part1, epoch+1
		if epoch == 10: part1 = abs(len(elfs) - get_area(elfs))

		# update elfs positions and cycle direction checks
		elfs = new_elfs
		_direc = check_direcs.pop(0)
		check_direcs.append(_direc)



data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1, ans2 = solve(data.copy())
print(ans1)
print(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))