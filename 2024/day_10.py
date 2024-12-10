from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def BFS(grid, start, p2=False):
	seen = set()
	q = deque([start])
	count = 0

	while q:
		node = q.popleft()
		if p2 or node not in seen:
			seen.add(node)

			if grid.get(node) == 9: count += 1

			q.extend([n for n in grid.get_neighbour_coords(node) if (grid.get(n) - grid.get(node) == 1)])

	return count


def part1(x):
	grid = aoc.Grid(x, cell_type=int)
	return sum([BFS(grid, s) for s in grid.find(0)])


def part2(x):
	grid = aoc.Grid(x, cell_type=int)
	return sum([BFS(grid, s, True) for s in grid.find(0)])


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