from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
import heapq
from tqdm import tqdm
import pyperclip
import aoc
from shapely import Polygon


def part1(x):
	points = [aoc.ints(line) for line in x]
	ans = 0

	for p1, p2 in itertools.combinations(points, 2):
		(x1, y1), (x2, y2) = p1, p2
		area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
		ans = max(ans, area)
	
	return ans


def _part2(x):
	points = [aoc.ints(line) for line in x]

	polygon = Polygon(points)
	ans = 0

	for p1, p2 in itertools.combinations(points, 2):
		(x1, y1), (x2, y2) = p1, p2
		area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
		if polygon.contains(Polygon([p1, (x2, y1), p2, (x1, y2)])):
			ans = max(ans, area)
	
	return ans


def lines_intersect(seg1, seg2, cross=False):
	x1, y1 = seg1[0]
	x2, y2 = seg1[1]
	x3, y3 = seg2[0]
	x4, y4 = seg2[1]

	if x1 > x2 or y1 > y2:
		x1, x2 = min(x1, x2), max(x1, x2)
		y1, y2 = min(y1, y2), max(y1, y2)
	if x3 > x4 or y3 > y4:
		x3, x4 = min(x3, x4), max(x3, x4)
		y3, y4 = min(y3, y4), max(y3, y4)

	if not cross:
		# both horizontal
		if y1 == y2 == y3 == y4: return not (x2 < x3 or x4 < x1)

		# both vertical
		if x1 == x2 == x3 == x4: return not (y2 < y3 or y4 < y1)

	# A is horizontal, B is vertical
	if y1 == y2 and x3 == x4: return (x3 > x1 and x3 < x2) and (y1 > y3 and y1 < y4)

	# A is vertical, B is horizontal
	if x1 == x2 and y3 == y4: return (x1 > x3 and x1 < x4) and (y3 > y1 and y3 < y2)

	return False


def valid_point(p, lines):
	inf_lines = [
		[ [-100, p[1]], p ],
   		[ p, [1_000_000, p[1]] ],
		[ [p[0], -100], p ],
  		[ p, [p[0], 1_000_000] ]
	]

	for l in inf_lines:
		for line in lines:
			if lines_intersect(l, line): break
		else:
			return False
	
	return True


def box_valid(p1, p2, p3, p4, lines):
	for box_line in [[p1, p3], [p1, p4], [p2, p3], [p2, p4]]:
		for line in lines:
			if lines_intersect(box_line, line, True):
				return False
	
	return True


def part2(x):
	points = [aoc.ints(line) for line in x]
	lines = []

	for p1, p2 in itertools.combinations(points, 2):
		if p1[0] == p2[0] or p1[1] == p2[1]: lines.append((p1, p2))
	
	ans = 0
	
	for p1, p2 in itertools.combinations(points, 2):
		(x1, y1), (x2, y2) = p1, p2
		p3, p4 = [x2, y1], [x1, y2]
		area = (abs(x1-x2)+1) * (abs(y1-y2)+1)

		if area <= ans: continue

		if valid_point(p3, lines) and valid_point(p4, lines):
			if box_valid(p1, p2, p3, p4, lines):
				ans = area

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
