from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def search_direc(grid, point, d):
	(r, c) = point
	for l in ['X', 'M', 'A', 'S']:
		if grid.valid(r, c) and grid.get((r, c)) == l:
			r, c = r+d[0], c+d[1]
		else:
			return False
	return True


def find_xmas(grid, point):
	direcs = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]

	return sum(search_direc(grid, point, d) for d in direcs)


def find_mas(grid, point):
	(r, c) = point
	_tr, _tl, _br, _bl = [(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]

	for (r, c) in [_tr, _tl, _br, _bl]:
		if not grid.valid(r, c): return False

	if grid.get(point) != "A": return False

	tr = grid.get(_tr)
	tl = grid.get(_tl)
	br = grid.get(_br)
	bl = grid.get(_bl)

	d1 = (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')
	d2 = (tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')

	return (d1 and d2)


def part1(x):
	grid = aoc.Grid(x)
	return sum(find_xmas(grid, p) for p in grid.all_points())


def part2(x):
	grid = aoc.Grid(x)
	return sum(find_mas(grid, p) for p in grid.all_points())


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