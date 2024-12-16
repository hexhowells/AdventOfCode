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


class Grid(aoc.Grid):
	def __init__(self, x):
		super().__init__(x)

	def get_neighbour_coords(self, point):
		(r, c) = point
		neighbour_cells = [(r-1, c, '^'), (r+1, c, 'v'), (r, c-1, '<'), (r, c+1, '>')]

		n = []
		for (r, c, d) in neighbour_cells:
			if self.valid(r, c):
				n.append( ((r, c), d) )

		return n



def dijkstra(grid, start, goal):
	distances = {node: float('infinity') for node in grid.all_points()}
	distances[start] = 0

	pq = [(0, start, '>')]

	while pq:
		curr_dist, curr_node, curr_direc = heapq.heappop(pq)

		if curr_node == goal:
			return curr_dist, distances

		if curr_dist > distances[curr_node]:
			continue

		for n, direc in grid.get_neighbour_coords(curr_node):
			if grid.get(n) == '#':
				continue

			dist = curr_dist + 1 + (1000 * int(direc != curr_direc))

			if dist < distances[n]:
				distances[n] = dist
				heapq.heappush(pq, (dist, n, direc))

	return -1


def search(grid, start, end, max_score, distances):
	q = deque([(start, '>', 0, [])])
	paths = []

	while q:
		node, curr_direc, curr_dist, curr_path = q.pop()

		if curr_dist-1000 > distances[node]:  # path not going to reach the end
			continue

		if node == end:
			paths.append(curr_path)
			continue

		for n, direc in grid.get_neighbour_coords(node):
			if grid.get(n) == '#':
				continue

			dist = curr_dist + 1 + (1000 * int(direc != curr_direc))

			if dist <= max_score:
				q.append((n, direc, dist, curr_path + [node]))

	return paths


def solve(x):
	grid = Grid(x)

	start = grid.find('S')[0]
	end = grid.find('E')[0]

	p1, dists = dijkstra(grid, start, end)

	paths = search(grid, start, end, p1, dists)
	p2 = set(itertools.chain.from_iterable(paths))

	return p1, len(p2)+1


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