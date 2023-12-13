from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def find_diffs(grid, i):
	diff = 0
	for j in range( min(i+1, grid.height-(i+1)) ):
		diff += sum( [x != y for x, y in zip(grid[i-j], grid[i+j+1])] )
	
	return diff


def find_row_relfection(grid, smudge=False):
	for i in range(len(grid.grid)-1):
		if find_diffs(grid, i) == int(smudge):
			return i + 1
		
	return -1


def part1(x):
	ans = 0

	for line in x:
		grid = aoc.Grid(line.split('\n'))
		if (row_split := find_row_relfection(grid)) != -1:
			ans += (row_split) * 100
		else:
			grid.transpose()
			ans += find_row_relfection(grid)

	return ans


def part2(x):
	ans = 0

	for line in x:
		grid = aoc.Grid(line.split('\n'))
		if (row_split := find_row_relfection(grid, smudge=True)) != -1:
			ans += (row_split) * 100
		else:
			grid.transpose()
			ans += find_row_relfection(grid, smudge=True)

	return ans


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n\n')))

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