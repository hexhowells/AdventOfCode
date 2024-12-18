from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
from tqdm import tqdm
import pyperclip
import aoc
import heapq


def dijkstra(grid, start, goal):
	distances = {node: float('infinity') for node in grid.all_points()}
	distances[start] = 0

	pq = [(0, start)]

	while pq:
		curr_dist, curr_node = heapq.heappop(pq)

		if curr_node == goal:
			return curr_dist

		if curr_dist > distances[curr_node]:
			continue

		for n in grid.get_neighbour_coords(curr_node):
			# avoid walls
			if grid.get(n) == '#': 
				continue

			dist = curr_dist + 1

			if dist < distances[n]:
				distances[n] = dist
				heapq.heappush(pq, (dist, n))

	return -1


def part1(x):
	grid = aoc.Grid([['.']*71]*71)

	for b in [aoc.ints(a) for a in x][:1024]:
		grid.set(b, '#')

	s, e = (0,0), (70, 70)

	return dijkstra(grid, s, e)


def part2(x):
	blocks = [aoc.ints(a) for a in x]
	grid = aoc.Grid([['.']*71]*71)

	for b in blocks[:1024]:
		grid.set(b, '#')

	s, e = (0,0), (70, 70)

	for b in blocks[1024:]:
		grid.set(b, '#')
		if dijkstra(grid, s, e) == -1:
			return ','.join(map(str, b))


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