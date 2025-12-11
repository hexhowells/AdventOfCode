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


@cache
def path(source, dest):
	paths = 0

	if source == dest: return 1
	if source == 'out': return 0
	
	paths = sum(path(p, dest) for p in path_map[source])
	
	return paths


def solve(x):
	global path_map
	path_map = {}
	for line in x:
		source, dests = line.split(': ')
		path_map[source] = dests.split(' ')

	p1 = path('you', 'out')
	p2 = path('svr', 'fft') * path('fft', 'dac') * path('dac', 'out') + \
			path('svr', 'dac') * path('dac', 'fft') *  path('fft', 'out')

	return p1, p2


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))