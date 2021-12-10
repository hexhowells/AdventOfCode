from collections import *
import math
import numpy as np
from timeit import default_timer as timer
from statistics import median


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


incomplete_chunks = []

def part1(x):
	invalid = []
	points = {"}": 1197, "]": 57, ")": 3, ">": 25137}
	closing_pair = {"{": "}", "[": "]", "(": ")", "<": ">"}

	for line in x:
		stack = []
		for c in list(line):
			if c in "{[(<":
				stack.append(c)
			else:
				if c != closing_pair[stack.pop()]:
					invalid.append(c)
					break
		else:
			incomplete_chunks.append(stack)

	return sum([points[x] for x in invalid])



def part2(x):
	scores = {"{": 3, "[": 2, "(": 1, "<": 4}
	points = []

	for chunk in incomplete_chunks:
		p = 0
		for c in reversed(chunk):
			p = (p * 5) + scores[c]
		points.append(p)

	sorted(points)
	return median(points)


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))