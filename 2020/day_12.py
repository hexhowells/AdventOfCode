from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def part1(x):
	n, e = 0, 0
	angle = 90
	angle_to_action = {0:'N', 90:'E', 180:'S', 270:'W'}

	for line in x:
		val = aoc.ints(line)[0]
		action = line.replace(str(val), "")

		if action == 'F':
			action = angle_to_action[angle]

		if action == 'R':
			angle = (angle + val) % 360
		elif action == 'L':
			angle = (angle - val) % 360
		elif action == 'N':
			n += val
		elif action == 'S':
			n -= val
		elif action == 'E':
			e += val
		elif action == 'W':
			e -= val

	return abs(n) + abs(e)


def rotate(point, origin, degrees):
    radians = np.deg2rad(degrees)
    x,y = point
    offset_x, offset_y = origin
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = np.cos(radians)
    sin_rad = np.sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + -sin_rad * adjusted_x + cos_rad * adjusted_y
    return qx, qy


def part2(x):
	way_n, way_e = 1, 10
	n, e = 0, 0
	angle = 90

	for line in x:
		val = aoc.ints(line)[0]

		if 'R' in line:
			way_e, way_n = rotate((way_e, way_n), (0,0), val)
		elif 'L' in line:
			way_e, way_n = rotate((way_e, way_n), (0,0), -val)

		elif 'F' in line:
			n += val * way_n
			e += val * way_e

		elif 'N' in line:
			way_n += val
		elif 'S' in line:
			way_n -= val
		elif 'E' in line:
			way_e += val
		elif 'W' in line:
			way_e -= val

	return math.ceil(abs(n) + abs(e))


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = [x for x in data.split('\n')]
#data = [int(x) for x in data.split('\n')]

start = timer()

# Part 1
ans1 = part1(data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))