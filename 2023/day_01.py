from collections import *
import math
#import numpy as np
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
		ints = aoc.ints(line)
		ans += int(str(ints[0])[0] + str(ints[-1])[-1])

	return ans


def convert(line):
	for i, digit in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
		line = line.replace(digit, digit[0] + str(i+1) + digit[-1])

	return line


def part2(x):
	ans = 0

	for line in x:
		ints = aoc.ints(convert(line))
		ans += int(str(ints[0])[0] + str(ints[-1])[-1])

	return ans


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

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