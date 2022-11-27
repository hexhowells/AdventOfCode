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
	target = int(x[0])
	times = [int(a) for a in x[1].replace('x,', '').split(",")]

	best = 1_000_000

	for t in times:
		if (val := t - (target % t)) < best:
			best = val
			ans = t * val

	return ans


def part2(x):
	times = [int(a) for a in x[1].replace('x', '1').split(",")]
	time, incr = 0, 1
	for i, bus in enumerate(times):
		while (time + i) % bus:
			time += incr
		incr *= bus

	return time


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