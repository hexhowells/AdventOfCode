from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def space_point(point, grid, acc):
	start_point = point

	while True:
		next_point = aoc.add_tuples(point, acc)
		next_point = (next_point[0]%grid.height, next_point[1]%grid.width)

		if grid.get(next_point) == '#': return start_point
		if grid.get(next_point) == '.': return next_point

		point = next_point


def move_point(point, grid, move, acc):
	for i in range(move):
		next_point = aoc.add_tuples(point, acc)
		next_point = (next_point[0]%grid.height, next_point[1]%grid.width)

		if grid.get(next_point) == '+': next_point = space_point(point, grid, acc)
		if grid.get(next_point) == '#': return point
		
		point = next_point

	return point


def format_grid(grid):
	grid = grid.replace(' ', '+').split('\n')
	width = max([len(grid[row]) for row in range(len(grid))])
	for row in range(len(grid)):
		grid[row] += '+' * (width - len(grid[row]))

	return grid


def part1(x):
	_grid, instructions = x
	_grid = format_grid(_grid)
	grid = aoc.Grid(_grid)
	
	direc_map = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}
	direc = 0
	
	# find top left corner
	point = (0, 0)
	for i in range(grid.width):
		if grid[0][i] == '.':
			point = (0, i)
			break

	instructions = instructions.replace('L', ' L ').replace('R', ' R ').split(" ")
	for ins in instructions:
		if ins == 'R': direc = (direc + 90) % 360
		elif ins == 'L': direc = (direc - 90) % 360
		else: point = move_point(point, grid, int(ins), direc_map[direc])

	return ((point[0]+1)*1000) + ((point[1]+1) * 4) + (direc//90)



#     curr_face         falling_edge       connected_face     connected_edge  
#        v                  v                   v                  v
edges = {0: {'N':(5, 'S'), 'E': (3, 'E'), 'S': (2, 'E'), 'W': (1, 'E')},
		 1: {'N':(5, 'W'), 'E': (0, 'W'), 'S': (2, 'N'), 'W': (4, 'W')},
		 2: {'N':(1, 'S'), 'E': (0, 'S'), 'S': (3, 'N'), 'W': (4, 'N')},
		 3: {'N':(2, 'S'), 'E': (0, 'E'), 'S': (5, 'E'), 'W': (4, 'E')},
		 4: {'N':(2, 'W'), 'E': (3, 'W'), 'S': (5, 'N'), 'W': (1, 'W')},
		 5: {'N':(4, 'S'), 'E': (3, 'S'), 'S': (0, 'N'), 'W': (1, 'N')}}


def change_face(grid, cur_face, falling_edge, point, edges):
	h, w = grid.height-1, grid.width-1
	row, col = point
	new_face = edges[cur_face][falling_edge][0]
	new_edge = edges[cur_face][falling_edge][1]

	if falling_edge == 'N' and new_edge == 'N': return new_face, (0, w-col), 90
	if falling_edge == 'N' and new_edge == 'E': return new_face, (h-col, w), 180
	if falling_edge == 'N' and new_edge == 'S': return new_face, (h, col), 270
	if falling_edge == 'N' and new_edge == 'W': return new_face, (col, 0), 0

	if falling_edge == 'E' and new_edge == 'N': return new_face, (0, w-row), 90
	if falling_edge == 'E' and new_edge == 'E': return new_face, (h-row, w), 180	
	if falling_edge == 'E' and new_edge == 'S': return new_face, (h, row), 270
	if falling_edge == 'E' and new_edge == 'W': return new_face, (row, 0), 0

	if falling_edge == 'S' and new_edge == 'N': return new_face, (0, col), 90
	if falling_edge == 'S' and new_edge == 'E': return new_face, (col, w), 180
	if falling_edge == 'S' and new_edge == 'S': return new_face, (h, w-col), 270
	if falling_edge == 'S' and new_edge == 'W': return new_face, (0, col), 0

	if falling_edge == 'W' and new_edge == 'N': return new_face, (0, row), 90
	if falling_edge == 'W' and new_edge == 'E': return new_face, (row, w), 180
	if falling_edge == 'W' and new_edge == 'S': return new_face, (h, w-row), 270
	if falling_edge == 'W' and new_edge == 'W': return new_face, (h-row, 0), 0


def has_fallen(point, grid, acc):
	new_point = (point[0]%grid.height, point[1]%grid.width)
	if point == new_point: return None
	if point[0] < new_point[0]: return 'N'
	if point[0] > new_point[0]: return 'S'
	if point[1] < new_point[1]: return 'W'
	if point[1] > new_point[1]: return 'E'


def move_point_on_cube(point, faces, face, move, direc):
	direc_map = { 0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0) }
	
	acc = direc_map[direc]
	faces[face] = faces[face]

	for i in range(move):
		next_point = aoc.add_tuples(point, acc)

		if (falling_edge := has_fallen(next_point, faces[face], acc)):
			new_face, next_point, new_direc = change_face(faces[face], face, falling_edge, point, edges)

			if faces[new_face].get(next_point) == '#': return point, face, direc

			face = new_face
			direc = new_direc
			acc = direc_map[direc]

		if faces[face].get(next_point) == '#': return point, face, direc
		point = next_point

	return point, face, direc


def part2(x):
	instructions = x.pop()

	faces = {}
	for i, face in enumerate(x):
		faces[i] = aoc.Grid(face.split("\n"))

	face = 1
	point = (0, 0)
	direc = 0

	instructions = instructions.replace('L', ' L ').replace('R', ' R ').split(" ")
	for ins in instructions:
		if ins == 'R': direc = (direc + 90) % 360
		elif ins == 'L': direc = (direc - 90) % 360
		else: point, face, direc = move_point_on_cube(point, faces, face, int(ins), direc)

	point = aoc.add_tuples(point, (0, 100))
	return ((point[0]+1)*1000) + ((point[1]+1) * 4) + (direc//90)


	return "Part 2 Empty"


data1 = collect_input("input.txt")
data1 = list(map(str, data1.split('\n\n')))

data2 = collect_input("input2.txt")
data2 = list(map(str, data2.split('\n\n')))

start = timer()

# Part 1
ans1 = part1(data1.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data2.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))