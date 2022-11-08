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


def part1(x):
	grid = aoc.Grid(x, str)

	col, row = 0, 0
	ans = 0
	while row < grid.height-1:
		row += 1
		col = (col+3) % grid.width
		
		if grid[row][col] == '#':
			ans +=1

	return ans


def part2(x):
	grid = aoc.Grid(x, str)

	trees = []
	for xx, yy in zip([1,3,5,7,1], [1,1,1,1,2]):
		x, y = 0, 0
		ans = 0
		while y < grid.height-1:
			x += xx
			y += yy
			
			x = x % grid.width
			
			if grid[y][x] == '#':
				ans += 1

		trees.append(ans)

	return math.prod(trees)


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = [x for x in data.split('\n')]
#data = [int(x) for x in data.split('\n')]

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