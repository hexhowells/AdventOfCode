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


def update_blizzards(blizzards, mins, h, w):
	new_blizzards = set()
	for (mv, r, c) in blizzards:
		if mv == '>':
			new_c = (((c-1) + mins) % w) + 1
			new_blizzards.add((r, new_c))
		elif mv == '<':
			new_c = (((c-1) - mins) % w) + 1
			new_blizzards.add((r, new_c))
		elif mv == 'v':
			new_r = (((r-1) + mins) % h) + 1
			new_blizzards.add((new_r, c))
		elif mv == '^':
			new_r = (((r-1) - mins) % h) + 1
			new_blizzards.add((new_r, c))

	return new_blizzards


def solve(grid, start, end, start_mins):
	walls = set()
	blizzards = set()
	for (r, c) in grid.all_points():
		if grid[r][c] == '#': walls.add((r, c))
		elif grid[r][c] == '.': pass
		else: blizzards.add((grid[r][c], r, c))

	height = grid.height - 2
	width = grid.width - 2

	q = deque()
	q.append((start, start_mins))
	visited = set()
	blizzard_cache = {}

	while q:
		v, mins = q.popleft()
		
		if (v, mins) in visited: continue
		visited.add((v, mins))

		if v == end: return mins
		mins += 1

		if mins in blizzard_cache:
			new_blizzards = blizzard_cache[mins]
		else:
			new_blizzards = update_blizzards(blizzards, mins, height, width)
			blizzard_cache[mins] = new_blizzards

		for acc in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
			new_v = (v[0]+acc[0], v[1]+acc[1])
			if (new_v not in walls) and (new_v not in new_blizzards) and (grid.valid(new_v[0], new_v[1])):
				q.append((new_v, mins))


def part1(x):
	grid = aoc.Grid(x)
	return solve(grid, (0, 1), (grid.height-1, grid.width-2), 0)


def part2(x, mins):
	grid = aoc.Grid(x)
	mins = solve(grid, (grid.height-1, grid.width-2), (0, 1), mins)
	return solve(grid, (0, 1), (grid.height-1, grid.width-2), mins)


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1 = part1(data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data.copy(), ans1)
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))