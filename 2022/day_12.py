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


def BFS(grid, start, end_char, condition):
	height_map = {'S':0, 'E':25}
	for i, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
		height_map[char] = i

	q = deque([start])
	explored = set([start])
	steps = {start:0}

	while q:
		v = q.popleft()
		char = grid.get(v)
		h = height_map[char]

		if char == end_char:
			return steps[v]

		for n in grid.get_neighbour_coords(v):
			if n not in explored:
				n_h = height_map[grid.get(n)]

				if condition(n_h, h):
					q.append(n)
					explored.add(n)
					steps[n] = steps[v] + 1


def part1(x):
	grid = aoc.Grid(x)
	start = (0, 0)
	
	for r, c in grid.all_points():
		if grid[r][c] == "S": start = (r, c)
	
	length = BFS(grid, start, "E", lambda a, b: a - b <= 1)

	return length


def part2(x):
	grid = aoc.Grid(x)
	start = (0, 0)
	
	for r, c in grid.all_points():
		if grid[r][c] == "E": start = (r, c)
	
	length = BFS(grid, start, "a", lambda a, b: b - a <= 1)

	return length


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