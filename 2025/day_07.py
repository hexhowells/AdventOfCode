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
	m = aoc.Grid(x)
	s = m.find('S')[0]
	seen = set()

	beams = [s]
	ans = 0

	while beams:
		b = beams.pop()

		if b in seen: continue
		seen.add(b)

		nbr, nbc = b[0]+1, b[1]

		if not m.valid(nbr, nbc): continue

		if m.get((nbr, nbc)) == '^':
			ans += 1
			beams.append((nbr, nbc-1))
			beams.append((nbr, nbc+1))
		else:
			beams.append((nbr, nbc))

	return ans


@cache
def search(m, b):
	nbr, nbc = b[0]+1, b[1]

	if not m.valid(nbr, nbc): return 1

	if m.get((nbr, nbc)) == '^':
		return sum([search(m, (nbr, nbc+acc)) for acc in [-1, 1]])
	else:
		return search(m, (nbr, nbc))


def part2(x):
	m = aoc.Grid(x)
	s = m.find('S')[0]

	return search(m, s)


def solve(x):
	row = [0] * len(x[0])
	row[x[0].index('S')] = 1
	p1 = 0

	for r in x[1:]:
		for i in [i for i, s in enumerate(r) if s == '^']:
			for acc in (-1, 1): row[i+acc] += row[i]
			if row[i] != 0: p1 += 1
			row[i] = 0
	
	return p1, sum(row)


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