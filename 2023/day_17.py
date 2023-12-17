from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import heapq


neighbours_mem = {}

def get_neighbours(grid, point):
	if point in neighbours_mem: return neighbours_mem[point]

	(r, c) = point
	neighbour_cells = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]

	n = []
	for (r, c), direc in zip(neighbour_cells, ['N', 'E', 'S', 'W']):
		if grid.valid(r, c):
			n.append( ((r, c), direc) )

	neighbours_mem[point] = n
	return n


def dijkstra(grid, start, goal, p2=False):
	distances = {}
	opp_direc = {'N':'S', 'S':'N', 'W':'E', 'E':'W', '':''}

	q = [(0, start, '', -1)]

	while q:
		curr_cost, curr_point, curr_direc, curr_count = heapq.heappop(q)

		if curr_point == goal: return curr_cost

		key = (curr_point[0], curr_point[1], curr_direc, curr_count)
		if key in distances: continue
		distances[key] = curr_cost

		for new_p, direc in get_neighbours(grid, curr_point):
			n_count = 1 if direc != curr_direc else curr_count+1

			part1_check = (n_count<=3)
			part2_check = (n_count<=10 and (direc==curr_direc or curr_count>=4 or curr_count==-1))

			isvalid = (part2_check if p2 else part1_check)

			if isvalid and (direc != opp_direc[curr_direc]):
				cost = curr_cost + grid.get(new_p)
				heapq.heappush(q, (cost, new_p, direc, n_count))


def part1(x):
    grid = aoc.Grid(x, cell_type=int)

    start = (0,0)
    end = (grid.width-1, grid.height-1)
    dists = dijkstra(grid, start, end)
    
    return dists
    

def part2(x):
    grid = aoc.Grid(x, cell_type=int)

    start = (0,0)
    end = (grid.width-1, grid.height-1)
    dists = dijkstra(grid, start, end, p2=True)
    
    return dists


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