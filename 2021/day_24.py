from collections import *
import math
from timeit import default_timer as timer
import itertools
import re


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def ints(string):
	return int(string.split(" ")[-1])


def extract_vars(x):
	variables = []
	for block in x.split("inp w\n")[1:]:
		ins = block.split("\n")
		variables.append([ints(ins[i]) for i in [3,4,14]])

	return variables


def get_serial(rules, val, sign, check):
	serial = [0] * 14
	for rule in rules:
		idx1, idx2 = rule.idx1, rule.idx2

		if check(rule.offset): idx2, idx1 = idx1, idx2

		serial[idx1] = val
		serial[idx2] = val + (abs(rule.offset) * sign)

	return ''.join([str(s) for s in serial])


def get_rules(x):
	Rule = namedtuple("Rule", "idx1, idx2, offset")
	stack = []
	rules = []
	for i, (a, b, c) in enumerate(extract_vars(x)):
		if a == 1:
			stack.append((i, c))
		else:
			(ii, cc) = stack.pop()
			rules.append(Rule(i, ii, cc+b))

	return rules


def solutions(x):
	rules = get_rules(x)
	highest = get_serial(rules, 9, -1, lambda x: x < 0)
	lowest = get_serial(rules, 1, 1, lambda x: x > 0)
	return highest, lowest


data = collect_input("input.txt")

start = timer()

part1, part2 = solutions(data)
print("{}\n{}".format(part1, part2))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))