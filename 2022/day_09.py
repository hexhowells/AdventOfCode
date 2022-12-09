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


# Chebyshev distance
def dist(a, b):
	x_diff = abs(a[0] - b[0])
	y_diff = abs(a[1] - b[1])
	return max(x_diff, y_diff)


def move(knots, move):
	knots[0] = tuple(map(sum, zip(knots[0], move)))

	for i in range(len(knots)-1):
		prev_knot, curr_knot = knots[i], knots[i+1]

		if dist(curr_knot, prev_knot) > 1:
			if curr_knot[0] != prev_knot[0]:
				curr_knot[0] += 1 if prev_knot[0] > curr_knot[0] else -1
			if curr_knot[1] != prev_knot[1]:
				curr_knot[1] += 1 if prev_knot[1] > curr_knot[1] else -1


def solve(x, k):
	knots = [[0, 0] for _ in range(k)]
	positions = set()
	shift = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L':(0, -1)}

	for line in x:
		direc, steps = line.split(" ")
		for _ in range(int(steps)):
			move(knots, shift[direc])
			positions.add(tuple(knots[-1]))

	return len(positions)


def part1(x):
	return solve(x, 2)


def part2(x):
	return solve(x, 10)


data = collect_input("input.txt")
#data = collect_input("test_input2.txt")

data = list(map(str, data.split('\n')))

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