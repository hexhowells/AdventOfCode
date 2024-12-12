from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
from tqdm import tqdm
import pyperclip
import aoc


def flood_fill(grid, p):
	seen = set()
	q = deque([p])
	value = grid.get(p)

	while q:
		node = q.popleft()
		if grid.get(node) == value and node not in seen:
			seen.add(node)
			q.extend([n for n in grid.get_neighbour_coords(node) if n not in seen])

	return seen


def perimeter(coords):
	perimeter = 0

	for c in coords:
		perimeter += sum([aoc.add_tuples(c, acc) not in coords for acc in aoc.acc_2d])

	return perimeter


def check_edge(a, b, prev_a, prev_b, in_edge):
	new_edge = 0

	if a ^ b:
		in_edge = ((a == prev_a) and (b == prev_b))

		if not in_edge:
			in_edge = True
			new_edge = 1
	else:
		in_edge = False

	return new_edge, in_edge, a, b


def vertical_edges(grid, coords):
	edges = 0
	in_edge = False
	prev_a, prev_b = False, False

	for col in range(-1, grid.w):
		in_edge = False
		for row in range(grid.h):
			a = (row, col) in coords
			b = (row, col+1) in coords
			new_edge, in_edge, prev_a, prev_b = check_edge(a, b, prev_a, prev_b, in_edge)
			edges += new_edge
	
	return edges


def horizontal_edges(grid, coords):
	edges = 0
	in_edge = False
	prev_a, prev_b = False, False

	for row in range(-1, grid.h):
		in_edge = False
		for col in range(grid.w):
			a = (row, col) in coords
			b = (row+1, col) in coords
			new_edge, in_edge, prev_a, prev_b = check_edge(a, b, prev_a, prev_b, in_edge)
			edges += new_edge

	return edges


def border(grid, coords):
	return vertical_edges(grid, coords) + horizontal_edges(grid, coords)


def solve(x):
	grid = aoc.Grid(x)

	areas = []
	seen = set()

	for p in grid.all_points():
		if p not in seen:
			a = flood_fill(grid, p)
			areas.append(a)
			seen = seen.union(a)

	p1, p2 = 0, 0
	for a in areas:
		p1 += len(a) * perimeter(a)
		p2 += len(a) * border(grid, a)

	return p1, p2


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
#ans2 = part2(data if type(data) == str else data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))