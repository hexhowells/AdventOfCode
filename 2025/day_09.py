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


def part2(x):
	points = [aoc.ints(line) for line in x]

	polygon = Polygon(points)
	ans = 0

	for p1, p2 in itertools.combinations(points, 2):
		(x1, y1), (x2, y2) = p1, p2
		area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
		if polygon.contains(Polygon([p1, (x2, y1), p2, (x1, y2)])):
			ans = max(ans, area)
	
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
