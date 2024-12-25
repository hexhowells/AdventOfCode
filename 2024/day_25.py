from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
import heapq
from tqdm import tqdm
import pyperclip
import aoc


def fit(lock, key):
	for lr, lk in zip(lock, key):
		if lr + lk > 5:
			return False
	return True


def part1(x):
	locks, keys = [], []

	for line in x:
		grid = aoc.Grid(line.split('\n'))
		if grid.get((0,0)) == '#':
			locks.append(grid)
		else:
			keys.append(grid)

	locks_pins = [[c.count('#')-1 for c in lock.cols()] for lock in locks]
	keys_pins = [[c.count('#')-1 for c in key.cols()] for key in keys]


	return sum([fit(l, k) for k in keys_pins for l in locks_pins])


def part2(x):
	return "Merry Christmas!"


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