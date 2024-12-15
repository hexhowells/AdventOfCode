from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
from tqdm import tqdm
import pyperclip
import aoc


def move_robot_p1(pos, grid, m):
	move = True
	new_pos = aoc.add_tuples(pos, m)
	rem_robots = []
	new_robots = []

	while True:
		match grid.get(new_pos):
			case '#':
				rem_robots = []
				new_robots = []
				move = False
				break
			case '.':
				rem_robots.append(pos)
				new_robots.append(new_pos)
				break
			case 'O':
				rem_robots.append(pos)
				new_robots.append(new_pos)
				pos = new_pos
				new_pos = aoc.add_tuples(new_pos, m)

	# move robots to new positions
	for r in rem_robots: grid.set(r, '.')
	for n in new_robots: grid.set(n, 'O')

	return move, grid


def move_ud(grid, pos, m):
	rem_robots, new_robots = [], []
	q = [pos]

	while q:
		robot_pos = q.pop()

		# move robot
		new_pos_l = aoc.add_tuples(robot_pos, m)
		new_pos_r = aoc.add_tuples(new_pos_l, (0, 1))

		sym_l = grid.get(new_pos_l)
		sym_r = grid.get(new_pos_r)

		if sym_l == '#' or sym_r == '#':
			rem_robots, new_robots = [], []
			break	
		elif sym_l == '[':
			q.append(new_pos_l)  # add new robot to queue
		elif sym_l == ']':
			q.append(aoc.add_tuples(new_pos_l, (0, -1)))  # add new robot to queue
		
		if sym_r == '[':
			q.append(new_pos_r)  # add new robot to queue

		rem_robots.append(robot_pos)
		new_robots.append(new_pos_l)

	return rem_robots, new_robots


def move_right(grid, pos, m):
	rem_robots, new_robots = [], []
	new_pos = aoc.add_tuples(aoc.add_tuples(pos, m), m)

	while True:
		match grid.get(new_pos):
			case '#':
				rem_robots, new_robots = [], []
				break
			case '.':
				rem_robots.append(pos)
				new_robots.append(aoc.sub_tuples(new_pos, m))
				break
			case '[':
				rem_robots.append(pos)
				new_robots.append(aoc.sub_tuples(new_pos, m))
				pos = new_pos
				new_pos = aoc.add_tuples(aoc.add_tuples(new_pos, m), m)

	return rem_robots, new_robots


def move_left(grid, pos, m):
	rem_robots, new_robots = [], []
	new_pos = aoc.add_tuples(pos, m)

	while True:
		match grid.get(new_pos):
			case '#':
				rem_robots, new_robots = [], []
				break
			case '.':
				rem_robots.append(pos)
				new_robots.append(new_pos)
				break
			case _:  # push robot
				rem_robots.append(pos)
				new_robots.append(new_pos)
				pos = new_pos
				new_pos = aoc.add_tuples(aoc.add_tuples(new_pos, m), m)

	return rem_robots, new_robots


def move_robot(robot_pos, grid, m):
	if grid.get(robot_pos) == ']':
		robot_pos = aoc.add_tuples(robot_pos, (0, -1))

	# invoke different logic depending on the direction of movement
	if m == (0, 1):
		rem_robots, new_robots = move_right(grid, robot_pos, m)
	elif m == (0, -1):
		rem_robots, new_robots = move_left(grid, robot_pos, m)
	else:
		rem_robots, new_robots = move_ud(grid, robot_pos, m)

	# remove old robot positions
	for r in rem_robots:
		grid.set(r, '.')
		grid.set(aoc.add_tuples(r, (0, 1)), '.')

	# move robots to new positions
	for n in new_robots:
		grid.set(n, '[')
		grid.set(aoc.add_tuples(n, (0, 1)), ']')

	return len(rem_robots) != 0, grid


def show_grid(grid, pos):
	grid.set(pos, '@')
	print(grid)
	grid.set(pos, '.')


def part1(x):
	grid = aoc.Grid(x[0].split('\n'))
	moves = list(x[1].replace('\n', ''))

	move = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

	pos = grid.find("@")[0]
	grid.set(pos, '.')

	for m in moves:
		new_pos = aoc.add_tuples(pos, move[m])

		match grid.get(new_pos):
			case '.':
				pos = new_pos
			case '#':
				continue
			case 'O':
				player_moves, grid = move_robot_p1(new_pos, grid, move[m])
				if player_moves: pos = new_pos

	return sum([100 * r + c for (r, c) in grid.find('O')])


def part2(x):
	expand_table = str.maketrans({'#': '##', 'O': '[]', '.': '..', '@': '@.'})
	new_grid = [line.translate(expand_table) for line in x[0].split('\n')]

	grid = aoc.Grid(new_grid)
	moves = list(x[1].replace('\n', ''))

	move = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}

	pos = grid.find("@")[0]
	grid.set(pos, '.')

	for m in moves:
		new_pos = aoc.add_tuples(pos, move[m])

		match grid.get(new_pos):
			case '.':
				pos = new_pos
			case '#':
				continue
			case '[' | ']':
				player_moves, grid = move_robot(new_pos, grid, move[m])
				if player_moves: pos = new_pos

	return sum([100 * r + c for (r, c) in grid.find('[')])


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n\n')))

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