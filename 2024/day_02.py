from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def safe(n):
	if (n == sorted(n)) or (n == sorted(n, reverse=True)):
		return sum( [not(0 < abs(a - b) <= 3) for a, b, in zip(n, n[1:])] ) == 0
	else:
		return False


def check(n):
	return sum([safe(n[:i] + n[i+1:]) for i in range(len(n))])


def part1(x):
	return sum(safe(aoc.ints(line)) for line in x)


def part2(x):
	return sum(safe(aoc.ints(line)) or check(aoc.ints(line)) > 0 for line in x)


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