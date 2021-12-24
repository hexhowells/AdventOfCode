from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def part1(x):
	return "Part 1 Empty"


def part2(x):
	return "Part 2 Empty"


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))