from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def get_transmitters(grid):
	nodes = defaultdict(list)

	for p in grid.all_points():
		cell = grid.get(p)
		if cell != '.':
			nodes[cell].append(p)

	return nodes


def search(grid, r, c, rd, cd, antinodes):
	while grid.valid(r, c):
		antinodes.add((r, c)) 
		r, c = r+rd, c+cd


def part1(x):
	grid = aoc.Grid(x)
	
	nodes = get_transmitters(grid)
	antinodes = set()

	for coords in nodes.values():
		for i in range(len(coords)):
			for j in range(i+1, len(coords)):
				r1, c1 = coords[i]
				r2, c2 = coords[j]

				# check antinode in one direction
				an1 = ( r1+(r1-r2), c1+(c1-c2) )
				if grid.valid(*an1):
					antinodes.add(an1)

				# check antinode in other direction
				an2 = ((r2+(r2-r1)), (c2+(c2-c1)))
				if grid.valid(*an2):
					antinodes.add(an2)

	return len(antinodes)


def part2(x):
	grid = aoc.Grid(x)

	nodes = get_transmitters(grid)
	antinodes = set()

	for coords in nodes.values():
		for i in range(len(coords)):
			for j in range(i+1, len(coords)):
				rd, cd = aoc.sub_tuples(coords[i], coords[j])
				
				search(grid, *coords[i], rd, cd, antinodes)
				search(grid, *coords[i], -rd, -cd, antinodes)
				
		
	return len(antinodes)


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1 = part1(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data if type(data) == str else data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))