from collections import *
import math
import numpy as np


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def parse_data(x):
	points = []
	for raw_line in x:
		p = raw_line.replace(" -> ", ",")
		points.append([int(a) for a in p.split(',')])
	return points


diff = lambda a, b: abs(b-a)
sign = lambda a, b: np.sign(b-a)
count = lambda grid: sum([c>=2 for c in grid.values()])


def solution(x):
	grid1 = Counter()
	grid2 = Counter()

	for x1, y1, x2, y2 in x:
		y_diff = diff(y1, y2)
		x_diff = diff(x1, x2)

		x_sign = sign(x1, x2)
		y_sign = sign(y1, y2)
		
		for i in range(max(x_diff, y_diff)+1):
			x_pos = x1 + (i*x_sign)
			y_pos = y1 + (i*y_sign)
			
			if x1 == x2 or y1 == y2:
				grid1[(x_pos, y_pos)] += 1
			grid2[(x_pos, y_pos)] += 1

	return count(grid1), count(grid2)


data = collect_input("input.txt")
data = [x for x in data.split('\n')]
points = parse_data(data)

part1, part2 = solution(points)
print("{}\n{}".format(part1, part2))