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
	for (i, j) in itertools.combinations(range(len(x)), 2):
		if x[i] + x[j] == 2020:
			return x[i] * x[j]


def part2(x):
	for (i, j, k) in itertools.combinations(range(len(x)), 3):
		if (x[i] + x[j] + x[k]) == 2020:
			return x[i] * x[j] * x[k]


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