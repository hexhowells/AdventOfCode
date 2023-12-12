from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from functools import cache


@cache
def num_configs(seq, rules):
	seq = seq.lstrip('.')

	if len(seq) == 0: 
		return len(rules) == 0

	if len(rules) == 0: 
		return seq.count('#') == 0

	if seq[0] == '#':
		if len(seq) < rules[0] or '.' in seq[:rules[0]]:
			return 0
		elif len(seq) == rules[0]: 
			return len(rules) == 1
		elif seq[rules[0]] == '#':
			return 0
		elif len(seq) == rules[0]: 
			return len(rules) == 1

		return num_configs(seq[rules[0]+1:], rules[1:])

	return num_configs('#' + seq[1:], rules) + num_configs(seq[1:], rules)


def part1(x):
	ans = 0

	for line in x:
		springs = line.split(' ')[0]
		rules = aoc.ints(line)

		ans += num_configs(springs, tuple(rules))

	return ans


def part2(x):
	ans = 0

	for line in x:
		springs = line.split(' ')[0]
		rules = aoc.ints(line)

		ans += num_configs('?'.join(springs for _ in range(5)), tuple(rules * 5))

	return ans


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

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