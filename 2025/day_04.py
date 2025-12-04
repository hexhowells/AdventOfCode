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


def part1(x):
	ans = 0
	rolls = aoc.Grid(x)
	for p in rolls.all_points():
		if rolls.get(p) == '@':
			n = rolls.get_neighbours(p, diag=True)
			if n.count('@') < 4:
				ans += 1
	return ans


def part2(x):
	ans = 0
	rolls = aoc.Grid(x)

	while True:
		mv = []
		for p in rolls.all_points():
			if rolls.get(p) == '@':
				n = rolls.get_neighbours(p, diag=True)
				if n.count('@') < 4:
					mv.append(p)
					ans += 1
		
		if len(mv) == 0: break

		for p in mv:
			rolls.set(p, '.')

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