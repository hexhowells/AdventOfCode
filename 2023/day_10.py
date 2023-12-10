from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def find_start(grid):
	for (r, c) in grid.all_points():
		if grid[r][c] == 'S':
			return (r, c)


def get_start_symbol(grid, point):
	(r, c) = point
	cart = {
		'N': ['|', 'L', 'J'],
		'E': ['-', 'L', 'F'],
		'S': ['|', '7', 'F'],
		'W': ['-', '7', 'J']
	}

	if grid[r-1][c] in cart['S'] and grid[r+1][c] in cart['N']: return '|'
	elif grid[r-1][c] in cart['S'] and grid[r][c+1] in cart['W']: return 'L'
	elif grid[r-1][c] in cart['S'] and grid[r][c-1] in cart['E']: return 'J'
	elif grid[r][c-1] in cart['E'] and grid[r][c+1] in cart['W']: return '-'
	elif grid[r+1][c] in cart['N'] and grid[r][c+1] in cart['W']: return 'F'
	elif grid[r+1][c] in cart['N'] and grid[r][c-1] in cart['E']: return '7'


def get_valid_neighbours(grid, point):
	(r, c) = point
	n = []
	direcs = {
		'|': [(-1,0), (1,0)],
		'-': [(0,-1), (0,1)],
		'L': [(-1,0), (0,1)],
		'J': [(-1,0), (0,-1)],
		'7': [(1,0), (0,-1)],
		'F': [(1,0), (0,1)],
		}

	for (r_acc, c_acc) in direcs[grid[r][c]]:
		rr, cc = r + r_acc, c + c_acc
		if grid.valid(rr, cc) and grid[rr][cc] != '.':
			n.append((rr, cc))

	return n


def zoom_row(grid):
	new_grid = []
	neighbour_pairs = [
		('-', '7'), ('F', '-'), ('L', 'J'), ('F', '7'), 
		('F', 'J'), ('L', '7'), ('L', '-'), ('-', 'J'), ('-', '-')
	]

	for row in grid.grid:
		new_row = ""
		for i in range(len(row)-1):
			new_row += row[i]
			if (row[i], row[i+1]) in neighbour_pairs:
				new_row += '-'
			else: 
				new_row += '.'

		new_row += row[-1]
		new_grid.append(new_row)

	return new_grid


def zoom_col(grid):
	new_grid = []
	neighbour_pairs = [
		('|', '|'), ('|', 'L'), ('|', 'J'), ('7', '|'), 
		('F', '|'), ('7', 'L'), ('7', 'J'), ('F', 'L'), ('F', 'J')
	]

	for col in range(grid.height-1):
		new_row = ""
		new_grid.append(''.join(grid[:][col]))

		for row in range(grid.width):
			if (grid[col][row], grid[col+1][row]) in neighbour_pairs:
				new_row += '|'
			else: 
				new_row += '.'

		new_grid.append(new_row)

	new_grid.append(grid[:][-1])

	return new_grid


def BFS(grid, start):
	seen = set()
	max_dist = 0
	q = deque([(start, 0)])

	while q:
		v, dist = q.popleft()
		
		if v not in seen:
			seen.add(v)

			if dist > max_dist:
				max_dist = dist

			for n in get_valid_neighbours(grid, v):
				if n not in seen:
					q.append((n, dist+1))

	return max_dist, seen


def flood_fill(grid, point):
	edge = False
	seen = set()
	queue = deque([point])

	while queue:
		r, c = queue.popleft()

		if not grid.valid(r, c):
			edge = True
			continue

		if (r, c) not in seen and grid[r][c] == '.':
			seen.add((r, c))

			queue.append((r+1, c))
			queue.append((r-1, c))
			queue.append((r, c+1))
			queue.append((r, c-1))

	return seen, edge


def part1(x):
	grid = aoc.Grid(x)
	
	start = find_start(grid)
	start_symbol = get_start_symbol(grid, start)
	grid.set(start, start_symbol)
	
	ans, _ = BFS(grid, start)

	return ans


def part2(x):
	grid = aoc.Grid(x)

	# find and replace start symbol with correct pipe
	start = find_start(grid)
	start_symbol = get_start_symbol(grid, start)
	grid.set(start, start_symbol)

	# find path and replace all non-path symbols with '.'
	_, path = BFS(grid, start)

	for (rrr, ccc) in grid.all_points():
		if (rrr, ccc) not in path:
			grid[rrr][ccc] = '.'

	# explode the grid to twice the size
	grid = aoc.Grid(zoom_row(grid))
	grid = aoc.Grid(zoom_col(grid))

	seen = set()
	valid_points = set()

	# flood fill all points
	# any flood not touching the edge is valid
	for (r, c) in grid.all_points():
		if (r, c) not in seen and grid[r][c] == '.':
			_seen, edge = flood_fill(grid, (r, c))
			seen = seen | _seen

			if not edge:
				for (rr, cc) in _seen:
					if ((rr, cc) not in valid_points) and (rr % 2 ==0) and (cc % 2 == 0):
						valid_points.add((rr, cc))

	return len(valid_points)


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