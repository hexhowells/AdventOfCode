from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def in_wall(grain, wall, lim):
	return (grain in wall) or (grain[0] == lim)


def build_walls(x):
	wall = set()
	floor = 0

	# build walls
	for line in x:
		coords = line.split(" -> ")
		for i in range(1, len(coords)):
			c, r = aoc.ints(coords[i-1])
			cc, rr = aoc.ints(coords[i])

			floor = max(floor, r, rr)
			if r == rr:
				for new_c in range(min(c, cc), max(c, cc)+1):
					wall.add((r, new_c))
			else:
				for new_r in range(min(r, rr), max(r, rr)+1):
					wall.add((new_r, c))

	return wall, floor
	

def simulate(x, part1):
	wall, floor = build_walls(x)
	start = (0, 500)
	sand = set()
	path = [start]

	while True:
		grain_stopped = True
		grain = path[-1]

		# try to move sand grain
		for acc in [[1, 0], [1, -1], [1, 1]]:
			new_grain = (grain[0] + acc[0], grain[1] + acc[1])
			if (new_grain not in sand) and (not in_wall(new_grain, wall, floor+2)):
				path.append(new_grain)
				grain_stopped = False
				break

		if grain_stopped: sand.add(path.pop())
	
		# check to terminate simulation
		if part1 and grain[0] >= floor: break
		if not part1 and start in sand: break
		
	return len(sand)


def part1(x):
	return simulate(x, part1=True)


def part2(x):
	return simulate(x, part1=False)


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1 = part1(data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))