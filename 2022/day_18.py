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


def get_corners(cubes):
	min_p = [1000, 1000, 1000]
	max_p = [-1000, -1000, -1000]

	for i in range(len(cubes)):
		for k in range(3):
			min_p[k] = min(min_p[k], cubes[i][k])
			max_p[k] = max(max_p[k], cubes[i][k])

	return [v-1 for v in min_p], [p+1 for p in max_p]


def in_bounds(p, max_p, min_p):
	for i in range(3):
		if not (min_p[i] <= p[i] <= max_p[i]):
			return False
	return True


# flood fill the outside to find surface rocks
def flood_fill(cubes, min_p, max_p):
	flood = set()
	q = [(min_p[0], min_p[1], min_p[2])]
	surface = set()

	while q:
		coord = q.pop()
		flood.add(coord)
		if coord not in cubes:
			for acc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
				new_coord = (coord[0]+acc[0], coord[1]+acc[1], coord[2]+acc[2])
				if new_coord in cubes: surface.add(coord)
				if (new_coord not in flood) and (in_bounds(new_coord, max_p, min_p)): q.append(new_coord)

	return surface


def part1(x):
	cubes = set([tuple(aoc.ints(line)) for line in x])

	sides = len(cubes) * 6
	for cube in cubes:
		for acc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
			neighbour_cube = (cube[0]+acc[0], cube[1]+acc[1], cube[2]+acc[2])
			if neighbour_cube in cubes: sides -= 1

	return sides


def part2(x):
	cubes = [tuple(aoc.ints(line)) for line in x]

	min_p, max_p = get_corners(cubes)
	surface = flood_fill(set(cubes), min_p, max_p)
	sides = 0
	for cube in cubes:
		for acc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
			test_cube = (cube[0]+acc[0], cube[1]+acc[1], cube[2]+acc[2])
			if test_cube in surface: sides += 1
			
	return sides


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# # Part 1
ans1 = part1(data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))
