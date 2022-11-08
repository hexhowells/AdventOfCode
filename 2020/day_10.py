from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import copy


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def part1(x):
	one = 0
	three = 0
	adapters = [0] + sorted(x)

	for i in range(1, len(adapters)):
		if adapters[i] - adapters[i-1] == 1:
			one += 1
		else:
			three += 1

	return one * (three + 1)


def part2(x):
	adapters = sorted(x)
	adapters.append(adapters[-1] + 3)

	mem = {0:1}
	for adp in adapters:
		mem[adp] = mem.get(adp-1,0) + mem.get(adp-2,0) + mem.get(adp-3,0)

	return mem[max(adapters)]


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