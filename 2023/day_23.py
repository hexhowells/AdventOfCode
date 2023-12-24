from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import copy
import re
import functools


acc = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}


def get_neighbours(grid, node, seen):
	symbol = grid.get(node)
	if symbol != '.':
		n = aoc.add_tuples(node, acc[symbol])
		return [] if n in seen else [n]
	else:
		return [n for n in grid.get_neighbour_coords(node) if (grid.get(n) != '#') and (n not in seen)]


def get_connections(grid, point, junctions):
	connections = []

	def path(grid, point, seen, junctions):
		node = point
		steps = 1
		while not (node != point and node in junctions):
			seen.add(node)
			n = get_neighbours(grid, node, seen)
			
			if len(n) == 0: return 
			
			node = n[0]
			steps += 1

		connections.append((node, steps))

	# branch in each direction until another junction or dead-end is found
	for n in get_neighbours(grid, point, {}):
		path(grid, n, {point}, junctions)

	return connections


def get_junctions(grid):
	return [p for p in grid.all_points() if grid.get(p) != '#' and len(get_neighbours(grid, p, {})) > 2]


def build_graph(grid, junctions):
	graph = {}
	junctions_set = set(junctions)
	for p in junctions:
		graph[p] = get_connections(grid, p, junctions_set)

	return graph


def solve_graph(graph, start, end):
	paths = []

	def find_path(graph, start, end, seen, steps):
		if start == end:
			paths.append(steps)
			return

		neighbours = [n for n in graph[start] if n[0] not in seen]
		seen.add(start) 

		for n in neighbours:
			find_path(graph, n[0], end, copy.copy(seen), steps+n[1])
		return 
		

	find_path(graph, start, end, set(), 0)

	return max(paths)


def part1(x):
	grid = aoc.Grid(x)

	start, end = (0, 1), (grid.height-1, grid.width-2)

	junctions = [start, end]
	junctions.extend(get_junctions(grid))

	graph = build_graph(grid, junctions)
	
	return solve_graph(graph, start, end)


def part2(x):
	x = re.sub(r'[><^v]', '.', '\n'.join(x)).split('\n')
	grid = aoc.Grid(x)
	
	start, end = (0, 1), (grid.height-1, grid.width-2)

	junctions = [start, end]
	junctions.extend(get_junctions(grid))

	graph = build_graph(grid, junctions)
	
	return solve_graph(graph, start, end)


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