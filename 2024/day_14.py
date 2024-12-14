from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
from tqdm import tqdm
import pyperclip
import aoc
import time


def tree(points, width=33):
	# group points by row
	rows = defaultdict(list)
	for r, c, _, _ in points:
		rows[r].append(c)

	# check each row for a horizontal line of the given width
	for c_values in rows.values():
		c_values.sort()
		count = 1
		for i in range(1, len(c_values)):
			if c_values[i] == c_values[i-1] + 1:
				count += 1
				if count == width:
					return True
			else:
				count = 1

	return False


def part1(x):
	robots = [aoc.ints(line) for line in x]

	w, h = 101, 103

	for _ in range(100):
		for i, (px, py, vx, vy) in enumerate(robots):
			robots[i] = ((px+vx) % w, (py+vy) % h, vx, vy)

	q1, q2, q3, q4 = 0, 0, 0, 0

	for px, py, vx, vy in robots:
		if px < (w//2) and py < (h//2): q1 += 1
		elif px > (w//2) and py < (h//2): q2 += 1
		elif px > (w//2) and py > (h//2): q3 += 1
		elif px < (w//2) and py > (h//2): q4 += 1

	return q1 * q2 * q3 * q4


def part2(x):
	robots = [aoc.ints(line) for line in x]

	w, h = 101, 103

	for step in range(1, 1_000_000):
		for i, (px, py, vx, vy) in enumerate(robots):
			robots[i] = ((px+vx) % w, (py+vy) % h, vx, vy)

		if tree(robots):
			return step


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