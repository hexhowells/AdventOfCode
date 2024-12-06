from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


move = {'^': (-1, 0), 'v':(1, 0), '>':(0, 1), '<': (0, -1)}
turn = {'^': '>', 'v':'<', '>':'v', '<': '^'}


def find_start(grid):
	for s in ['^', 'v', '>', '<']:
		pos = grid.find(s)[0]
		if pos != None: 
			return pos, grid.get(pos)


def in_loop(grid, pos, direc):	
	r, c = pos
	seen = set()

	while True:
		if ((r, c), direc) in seen: return True
		seen.add(((r, c), direc))

		nr, nc = r+move[direc][0], c+move[direc][1]
		
		if not grid.valid(nr, nc):
			return False
		else:
			ns = grid.get((nr, nc))
			if ns == '#':
				direc = turn[direc]
			else:
				r, c = nr, nc


def get_path(grid, pos, direc):
	r, c = pos
	seen = set()

	while True:
		seen.add((r,c))
		nr, nc = r+move[direc][0], c+move[direc][1]
		
		if not grid.valid(nr, nc):
			break
		else:
			ns = grid.get((nr, nc))
			if ns == '#':
				direc = turn[direc]
			else:
				r, c = nr, nc
				
	return seen


def part1(x):
	grid = aoc.Grid(x)

	start, direc = find_start(grid)

	return len(get_path(grid, start, direc))


def part2(x):
	grid = aoc.Grid(x)

	start, direc = find_start(grid)

	search = get_path(grid, start, direc)
	search.remove(start)

	ans = 0

	for p in search:
		grid.set(p, '#')

		if in_loop(grid, start, direc): 
			ans += 1

		grid.set(p, '.')

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