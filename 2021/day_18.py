from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def parse(line):
	line = filter(lambda el: el != ',', line)
	tokens = [int(token) if token.isdigit() else token for token in line]
	return tokens


def magnitude(seq):
	p = 0
	while p < len(seq):
		token = seq[p]
		if token == "]":
			mag = (3*seq[p-2]) + (2 * seq[p-1])
			seq = seq[:p-3] + [mag] + seq[p+1:]
			p = 0
			continue
		p += 1
	return seq[0]


def explode(seq, p):
	left_num = seq[p]
	right_num = seq[p+1]

	for lp in range(p-1, 0, -1):
		if type(seq[lp]) == int:
			seq[lp] += left_num
			break

	for rp in range(p+2, len(seq)):
		if type(seq[rp]) == int:
			seq[rp] += right_num
			break

	return seq[:p-1] + [0] + seq[p+3:]


def split(seq, p):
	val = seq[p]
	left_val = math.floor(val/2)
	right_val = math.ceil(val/2)
	new_pair = ["[", left_val, right_val, "]"]

	return seq[:p] + new_pair + seq[p+1:]


def try_explode(seq):
	nested = 0
	for p, token in enumerate(seq):
		if nested == 4 and token == "[":
			seq = explode(seq, p+1)
			return True, seq
		elif token == "[":
			nested += 1
		elif token == "]":
			nested -= 1

	return False, seq


def try_split(seq):
	for p, token in enumerate(seq):
		if type(token) == int and token >= 10:
			seq = split(seq, p)
			return True, seq
	return False, seq


def compute(seq):
	has_reduced = True
	while has_reduced:
		has_reduced, seq = try_explode(seq)
		if not has_reduced:
			has_reduced, seq = try_split(seq)
	return seq


def part1(x):
	lines = [parse(line) for line in x]
	result = lines[0]
	for i in range(1, len(lines)):
		result = compute(["["] + result + lines[i] + ["]"])

	return magnitude(result)


def part2(x):
	lines = [parse(line) for line in x]
	best_result = 0
	for i in range(len(lines)):
		for j in range(i+1, len(lines)):
			for (a, b) in [(i, j), (j, i)]:
				result = magnitude( compute(["["] + lines[a] + lines[b] + ["]"]) )
				best_result = max(best_result, result)
	
	return best_result


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))