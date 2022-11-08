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


def get_ids(x):
	seat_ids = []

	for line in x:
		hi, lo, hi_c, lo_c = 127, 0, 7, 0

		for seat in line:
			if seat == 'F':
				hi -= math.ceil((hi-lo) / 2)
			if seat == 'B':
				lo += math.ceil((hi-lo) / 2)
			if seat == 'L':
				hi_c -= math.ceil((hi_c-lo_c) / 2)
			if seat == 'R':
				lo_c += math.ceil((hi_c-lo_c) / 2)

		seat_ids.append(hi * 8 + hi_c)

	return seat_ids


def part1(x):
	return max(get_ids(x))


def part2(x):
	all_seats = sorted(get_ids(x))
	for i, s in enumerate(all_seats[:-1]):
		if s+1 != all_seats[i+1]:
			return s+1


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