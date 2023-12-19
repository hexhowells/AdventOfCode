from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import operator
import copy


def valid(part, workflows):
	curr_rule = workflows['in']

	while True:
		for ch, comp, val, jmp in curr_rule:
			if ch == -1 or comp(part[ch], val):
				if jmp == 'A': return True
				if jmp == 'R': return False
				curr_rule = workflows[jmp]
				break


def get_workflows(x):
	workflows = {}
	ops = {'>': operator.gt, '<': operator.lt}

	for workflow in x[0].split('\n'):
		name, _rules = workflow.replace('}','').split('{')
		_rules = _rules.split(',')
		workflows[name] = []

		for r in _rules[:-1]:
			ch = r[0]
			comp = ops[r[1]]
			val = aoc.ints(r)[0]
			jmp = r.split(':')[1]
			workflows[name].append((ch, comp, val, jmp))

		workflows[name].append((-1, -1, -1, _rules[-1]))

	return workflows
	

def update_range(ranges, ch, comp, val):
	new_ranges = copy.deepcopy(ranges)
	if comp == operator.gt: 
		new_ranges[ch][0] = val + 1
	else: 
		new_ranges[ch][1] = val - 1

	return new_ranges


def num_valid(workflows):
	start_range = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
	#		  range,  next_workflow,  next_rule
	stack = [(start_range, 'in', 0)]
	ans = []

	while stack:
		ranges, rule, num = stack.pop()

		if rule == 'A':
			ans.append(ranges)
			continue
		if rule == 'R':
			continue

		ch, comp, val, jmp = workflows[rule][num]

		if ch == -1:
			stack.append((ranges, jmp, 0))
			continue

		ranges2 = update_range(ranges, ch, comp, val)
		stack.append((ranges2, jmp, 0))

		ranges[ch][1 if comp == operator.gt else 0] = val
		stack.append((ranges, rule, num + 1))

	return ans


def combinations(ranges):
	return sum(math.prod( [r[k][1] - r[k][0] + 1 for k in r] ) for r in ranges)


def part1(x):
	workflows = get_workflows(x)
	parts = []

	for line in x[1].split('\n'):
		vals = aoc.ints(line)
		parts.append({'x':vals[0], 'm':vals[1], 'a':vals[2], 's':vals[3]})

	return sum([sum(part.values()) for part in parts if valid(part, workflows)])


def part2(x):
	workflows = get_workflows(x)
	ranges = num_valid(workflows)

	return combinations(ranges)


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n\n')))

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