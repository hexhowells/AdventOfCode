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

	y_rules = set(range(max(y_coords))) - y_coords
	x_rules = set(range(max(x_coords))) - x_coords

	new_galaxies = []

	for (yy, xx) in galaxies:
		yy_expand = sum([1 for yr in y_rules if yy > yr])
		xx_expand = sum([1 for xr in x_rules if xx > xr])

		yy += expand_factor * yy_expand
		xx += expand_factor * xx_expand

		new_galaxies.append((yy, xx))

	return new_galaxies


def part1(x):
	grid = aoc.Grid(x)
	galaxies = grid.find('#')

	galaxies = expand(galaxies, 1)

	ans = 0
	for i in range(len(galaxies)):
		for j in range(i, len(galaxies)):
			ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

	return ans


def part2(x):
	grid = aoc.Grid(x)
	galaxies = grid.find('#')

	galaxies = expand(galaxies, 999_999)

	ans = 0
	for i in range(len(galaxies)):
		for j in range(i, len(galaxies)):
			ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

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