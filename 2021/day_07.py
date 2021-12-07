from collections import *
import math
import numpy as np
from statistics import median, mean


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def part1(x):
	m = int(median(x))
	return sum([abs(num-m) for num in x])


triangle = lambda n: n * (n + 1) // 2

def part2(x):
	m = int(mean(x))
	return sum([triangle(abs(num-m)) for num in x])


data = collect_input("input.txt")
data = [int(x) for x in data.split(',')]

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))