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
	ans = 0
	for line in x:
		a, b, c, d = aoc.ints(line.replace('-', ' '))

		if (a <= c and b >= d) or (c <= a and d >= b): 
			ans += 1

	return ans


def part2(x):
	ans = 0
	for line in x:
		a, b, c, d = aoc.ints(line.replace('-', ' '))

		if (a <= c <= b) or (c <= b <= d) or (c <= a <= d) or (a <= d <= b): 
			ans += 1
	
	return ans


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