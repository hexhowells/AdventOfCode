from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from tqdm import tqdm
from functools import cache


@cache
def shift_row(row_str, w):
	row = list(row_str)

	for i in range(w, -1, -1):
		if row[i] == 'O':
			j = i
			while j < w and row[j + 1] == '.':
				j += 1

			row[i], row[j] = row[j], row[i]

	return row


def shift(grid):
	grid.grid = [shift_row(''.join(row), grid.width-1) for row in grid.grid]


def cycle(grid):
	for _ in range(4):
		grid.rotate_90()
		shift(grid)


def part1(x):
	grid = aoc.Grid(x)

	grid.rotate_90()
	shift(grid)
	grid.transpose()

	return sum([r+1 for (r, c) in grid.find('O')])


def part2(x):
	grid = aoc.Grid(x)
	first_seen = {}

	for a in range(1_000_000_000):
		cycle(grid)
		grid_hash = str(grid)

		# cycle found
		if grid_hash in first_seen:
			new_range = (999_999_999 - a) % (a - first_seen[grid_hash])
			break
		
		first_seen[grid_hash] = a

	[cycle(grid) for _ in range(new_range)]

	return sum([grid.height-r for (r, c) in grid.find('O')])


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