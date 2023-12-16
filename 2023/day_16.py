from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def get_tiles(grid, pp, dd):
	direc = {'N': (-1,0), 'E': (0,1), 'S':(1,0), 'W':(0,-1)}
	stack = [(pp, dd)]
	seen = set()
	tiles = set()

	while stack:
		p, d = stack.pop()

		if (not grid.valid(p[0], p[1])) or ((p,d) in seen):
			continue

		if p not in tiles: tiles.add(p)

		seen.add((p,d))

		if grid.valid(p[0], p[1]):
			match grid.get(p):
				case '.':
					stack.append((aoc.add_tuples(p, direc[d]), d))
				case '-':
					if d == 'E' or d == 'W': 
						stack.append((aoc.add_tuples(p, direc[d]), d))
					else:
						stack.append((aoc.add_tuples(p, direc['E']), 'E'))
						stack.append((aoc.add_tuples(p, direc['W']), 'W'))
				case '|':
					if d == 'N' or d == 'S': 
						stack.append((aoc.add_tuples(p, direc[d]), d))
					else:
						stack.append((aoc.add_tuples(p, direc['N']), 'N'))
						stack.append((aoc.add_tuples(p, direc['S']), 'S'))
				case '/':
					match d:
						case 'N': stack.append((aoc.add_tuples(p, direc['E']), 'E'))
						case 'E': stack.append((aoc.add_tuples(p, direc['N']), 'N'))
						case 'S': stack.append((aoc.add_tuples(p, direc['W']), 'W'))
						case 'W': stack.append((aoc.add_tuples(p, direc['S']), 'S'))
				case "\\":
					match d:
						case 'N': stack.append((aoc.add_tuples(p, direc['W']), 'W'))
						case 'E': stack.append((aoc.add_tuples(p, direc['S']), 'S'))
						case 'S': stack.append((aoc.add_tuples(p, direc['E']), 'E'))
						case 'W': stack.append((aoc.add_tuples(p, direc['N']), 'N'))



	return len(tiles)


def part1(x):
	grid = aoc.Grid(x)

	return get_tiles(grid, (0,0), 'E')


def get_edges(width, height):
	top_edge = [(x, 0) for x in range(width)]
	bottom_edge = [(x, height - 1) for x in range(width)]
	left_edge = [(0, y) for y in range(0, height )]
	right_edge = [(width - 1, y) for y in range(0, height)]

	return top_edge, bottom_edge, left_edge, right_edge


def part2(x):
	grid = aoc.Grid(x)
	ans = 0

	l, r, t, b = get_edges(grid.width, grid.height)

	for p in t: ans = max(ans, get_tiles(grid, p, 'S'))
	for p in b: ans = max(ans, get_tiles(grid, p, 'N'))
	for p in l: ans = max(ans, get_tiles(grid, p, 'E'))
	for p in r: ans = max(ans, get_tiles(grid, p, 'W'))

	return ans


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