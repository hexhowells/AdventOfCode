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


def get_folder_sizes(x):
	path = []
	sizes = {'/': 0}
	
	for line in x:
		words = line.split()
		if words[1] == 'cd' and words[2] == '..': path.pop()
		elif words[1] == 'cd': path.append(words[-1])
		elif words[1] == 'ls': continue
		elif words[0] == 'dir': sizes[''.join(path) + line[4:]] = 0
		else:
			for p in itertools.accumulate(path):
				sizes[p] += int(words[0])

	return sizes


def part1(x):
	sizes = get_folder_sizes(x)
	return sum([v for v in sizes.values() if v <= 100_000])


def part2(x):
	sizes = get_folder_sizes(x)
	return min([v for v in sizes.values() if v >= (sizes['/'] - 40_000_000)])


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

#data = [x for x in data.split('\n\n')]
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