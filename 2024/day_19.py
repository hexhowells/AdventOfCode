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



def valid(towel, patterns):
	if len(towel) == 0:
		return True

	for p in patterns:
		if towel.startswith(p):
			if valid(towel[len(p):], patterns):
				return True

	return False


def count(towel, patterns, mem):
	if len(towel) == 0:
		return 1

	if towel in mem:
		return mem[towel]

	total = 0
	for p in patterns:
		if towel.startswith(p):
			total += count(towel[len(p):], patterns, mem)

	mem[towel] = total

	return total


def part1(x):
	patterns = x[0].split(', ')
	towels = x[1].split('\n')

	return sum(valid(t, patterns) for t in towels)


def part2(x):
	patterns = x[0].split(', ')
	towels = x[1].split('\n')

	return sum(count(t, patterns, {}) for t in towels)


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