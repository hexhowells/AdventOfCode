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


def match(values, target):
	for x, y in itertools.combinations(values, 2):
		if x + y == target:
			return True
	return False


def part1(x):
	for i in range(25, len(x)):
		if not match(x[i-25:i], x[i]):
			return x[i]


def part2(x):
	target = 507622668  # taken from part1 answer

	i, j = 0, 1
	while j < len(x):
		val = sum(x[i:j+1])

		if val == target:
			return min(x[i:j+1]) + max(x[i:j+1])
		elif val > target:
			i += 1
		else:
			j += 1


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

#data = [x for x in data.split('\n')]
data = [int(x) for x in data.split('\n')]

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