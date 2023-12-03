from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def valid(grid, n):
	return [(r, c) for (r, c) in n if grid[r][c].isdigit()]


def get_part_number(grid, p):
	width = len(grid[0])
	(r, c) = p
	start_idx, end_idx = c, c

	while start_idx != 0 and grid[r][start_idx-1].isdigit():
		start_idx -= 1

	while end_idx < width and grid[r][end_idx].isdigit():
		end_idx += 1

	return (r, start_idx), int(''.join(grid[r][start_idx:end_idx]))


def part1(x):
	ans = 0
	seen = set()
	grid = aoc.Grid(x)

	for (r, c) in grid.all_points():
		if grid[r][c] != '.' and not grid[r][c].isdigit():
			p = valid(grid, grid.get_neighbour_coords((r, c), True))
			for pp in p:
				start_p, part_number = get_part_number(grid, pp)
				if start_p not in seen:
					ans += part_number
					seen.add(start_p)
	return ans


def part2(x):
	ans = 0
	grid = aoc.Grid(x)

	for (r, c) in grid.all_points():
		seen = set()
		if grid[r][c] == '*':
			p = valid(grid, grid.get_neighbour_coords((r, c), True))
			for pp in p:
				start_p, part_number = get_part_number(grid, pp)
				if start_p not in seen:
					seen.add(start_p)

			if len(seen) == 2:
				ans += math.prod([get_part_number(grid, pp)[1] for pp in seen])

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