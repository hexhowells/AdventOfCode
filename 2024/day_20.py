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


def BFS(grid, start, end):
	seen = set()
	q = deque([(start, [])])

	while q:
		node, path = q.popleft()

		if node == end:
			return path+[end]

		if node not in seen:
			seen.add(node)
			for n in grid.get_neighbour_coords(node):
				if n not in seen and grid.get(n) != '#':
					q.append((n, path+[node]))

	return []


def solve(x):
	grid = aoc.Grid(x)
	s = grid.find('S')[0]
	e = grid.find('E')[0]

	path = BFS(grid, s, e)

	p1, p2 = 0, 0
	for i in range(len(path)-1):
		for j in range(i+1, len(path)):
			d = grid.dist(path[i], path[j])
			if d <= 2:
				p1 += int(((j-i)-d) >= 100)
			if d <= 20:
				p2 += int(((j-i)-d) >= 100)

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
#ans2 = part2(data if type(data) == str else data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))