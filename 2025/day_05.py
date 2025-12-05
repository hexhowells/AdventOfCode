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


def merge(r1, r2):
	l1, h1 = r1
	l2, h2 = r2

	if (l1 <= l2 <= h1): return (l1, max(h1,h2))
	if (l2 <= l1 <= h2): return (l2, max(h1,h2))

	return None


def solve(x):
	# part 2
	ranges = [tuple(aoc.ints(line, neg=False)) for line in x[0].split('\n')]
	ranges = sorted(ranges, key=lambda x: x[0])

	for i in range(len(ranges)-1):
		mr = merge(ranges[i], ranges[i+1])
		if mr is not None:
			ranges[i] = None
			ranges[i+1] = mr
		
	ranges = list(filter(None, ranges))
	p2 = sum([(h-l) + 1 for (l, h) in ranges])

	# part 1
	p1 = 0
	for num in x[1].split('\n'):
		for (l, h) in ranges:
			if l <= int(num) <= h:
				p1 += 1
				break
	
	return p1, p2


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n\n')))

start = timer()

# Part 1 & 2
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))