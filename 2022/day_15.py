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


def manhattan_dist(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part1(x):
	sensors, beacons = [], []
	dists = {}
	min_x, max_x, max_dist = int(1e9), -int(1e9), -1

	for line in x:
		sx, sy, bx, by = aoc.ints(line)
		
		sensors.append((sx, sy))
		beacons.append((bx, by))

		dists[(sx, sy)] = manhattan_dist((sx, sy), (bx, by))

		min_x = min(min_x, sx)
		max_x = max(max_x, sx)
		max_dist = max(max_dist, dists[(sx, sy)])

	ans = 0
	y = 2_000_000 #10
	for i in range(min_x - max_dist, max_x+max_dist+1):
		for sensor in sensors:
			if manhattan_dist(sensor, (i, y)) <= dists[sensor] and (i, y) not in beacons:
				ans += 1
				break

	return ans


def part2(x):
	sensors, points = [], []
	dists = {}
	lim = 4000000 #20

	for line in x:
		sx, sy, bx, by = aoc.ints(line)
		d = manhattan_dist((sx, sy), (bx, by))
		sensors.append((sx, sy))
		dists[(sx, sy)] = d

		# get taxicab circle of the sensor range border
		d += 1
		for i in range(0, d):
			if 0<=sx+i<=lim and 0<=sy+(d-i)<=lim: points.append((sx+i, sy+(d-i)))
			if 0<=sx-i<=lim and 0<=sy+(d-i)<=lim: points.append((sx-i, sy+(d-i)))
			if 0<=sx+i<=lim and 0<=sy-(d-i)<=lim: points.append((sx+i, sy-(d-i)))
			if 0<=sx-i<=lim and 0<=sy-(d-i)<=lim: points.append((sx-i, sy-(d-i)))

	for p in points:
		for sensor in sensors:
			if manhattan_dist(sensor, p) <= dists[sensor]: break
		else:
			return p[0] * 4000000 + p[1]


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

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