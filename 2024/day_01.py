from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def part1(x):
	l1, l2 = [], []
	for line in x:
		a, b = line.split()
		l1.append(int(a))
		l2.append(int(b))

	l1 = sorted(l1)
	l2 = sorted(l2)

	return sum([abs(a - b) for a, b in zip(l1, l2)])


def part2(x):
	l1, l2 = [], []
	for line in x:
		a, b = line.split()
		l1.append(int(a))
		l2.append(int(b))

	return sum([l * l2.count(l) for l in l1])


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
