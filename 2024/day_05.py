from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def valid(p, rules):
	for i in range(1, len(p)):
		for j in range(i):
			if f'{p[i]}|{p[j]}' in rules: return False
		
	return True


def fix(p, rules):
	for i in range(1, len(p)):
		for j in range(i):
			if f'{p[i]}|{p[j]}' in rules:
				p.insert(j, p.pop(i))

	return p


def solve(x):
	pages = [aoc.ints(l) for l in x[1].split('\n')]
	rules = set(x[0].split('\n'))

	p1, p2 = 0, 0

	for p in pages:
		if valid(p, rules):
			p1 += p[(len(p)) // 2]
		else:
			fix(p, rules)
			p2 += p[(len(p)) // 2]

	return p1, p2


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n\n')))

start = timer()

# Part 1
ans1, ans2 = solve(data if type(data) == str else data.copy())
#ans1 = part1(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
#ans2 = part2(data if type(data) == str else data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))