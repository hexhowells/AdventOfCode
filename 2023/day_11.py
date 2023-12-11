from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def expand(galaxies, expand_factor):
	y_coords = set([a[0] for a in galaxies])
	x_coords = set([a[1] for a in galaxies])

	y_space = set(range(max(y_coords))) - y_coords
	x_space = set(range(max(x_coords))) - x_coords

	new_galaxies = []

	for (yy, xx) in galaxies:
		y_expand = sum([yy > yr for yr in y_space]) * expand_factor
		x_expand = sum([xx > xr for xr in x_space]) * expand_factor

		new_galaxies.append(aoc.add_tuples( (yy, xx), (y_expand, x_expand) ))

	return new_galaxies


def solve(x, expand_factor):
	grid = aoc.Grid(x)
	galaxies = grid.find('#')

	galaxies = expand(galaxies, expand_factor)

	return sum([abs(ax-bx) + abs(ay-by) for (ax, ay), (bx, by) in itertools.combinations(galaxies, 2)])


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1 = solve(data if type(data) == str else data.copy(), 1)
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = solve(data if type(data) == str else data.copy(), 999_999)
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))