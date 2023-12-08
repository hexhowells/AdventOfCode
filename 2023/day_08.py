from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def get_lookup(x):
	lookup = {}

	for line in x.split('\n'):
		opcode, raw = line.split(" = ")
		l_op, r_op = raw.split(', ')
		lookup[opcode] = [l_op[1:], r_op[:-1]]

	return lookup


def get_steps(node, lookup, ins, func):
	len_ins = len(ins)
	ptr, steps = 0, 0

	while True:
		next_ins = ins[ptr % len_ins]
		node = lookup[node][next_ins]

		steps += 1
		ptr += 1

		if func(node):
			return steps


def part1(x):
	ins = list(map(lambda a: 1 if a=='R' else 0, list(x[0])))
	lookup = get_lookup(x[1])

	return get_steps('AAA', lookup, ins, lambda n: n == 'ZZZ')


def part2(x):
	ins = list(map(lambda a: 1 if a=='R' else 0, list(x[0])))
	lookup = get_lookup(x[1])

	nodes = [v for v in lookup.keys() if v[2] == 'A']
	num_steps = [get_steps(n, lookup, ins, lambda n: n[2] == 'Z') for n in nodes]

	return math.lcm(*num_steps)



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