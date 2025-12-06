from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
import heapq
from tqdm import tqdm
import pyperclip
import aoc


def part1(x):
	cols = defaultdict(list)
	ops = {}

	for row in x[:-1]:
		for i, val in enumerate(aoc.ints(row)):
			cols[i].append(val)
	
	for i, s in enumerate(x[-1].replace(' ', '')):
		ops[i] = s

	ans = 0
	for k, v in cols.items():
		if ops[k] == '+': ans += sum(v)
		elif ops[k] == '*': ans += math.prod(v)
	
	return ans


def part2(x):
	cols = defaultdict(str)
	ops = {}

	for row in x[:-1]:
		for i, val in enumerate(row):
			cols[i] += (val)
	
	cols[len(cols.keys()) + 1] += ' '

	for i, s in enumerate(x[-1]):
		ops[i] = s

	ans = 0
	op = None
	bank = []
	for k, v in cols.items():
		if k in ops and ops[k] != ' ':
			op = ops[k]
		
		if set(v) == {' '}:
			if op == '+': ans += sum(bank)
			elif op == '*': ans += math.prod(bank)
			bank = []
		else:
			bank.append(int(v))
	
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