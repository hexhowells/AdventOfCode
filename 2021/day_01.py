from collections import *
import math

def collect_input():
	with open("input.txt") as inputfile:
		data = inputfile.read()

	return data.rstrip()


def part1(x):
	return sum([x[i] > x[i-1] for i in range(1, len(x))])


def part2(x):
	return sum([x[i] > x[i-3] for i in range(3, len(x))])


# Input
data = collect_input()
data = [int(x) for x in data.split('\n')]

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))

