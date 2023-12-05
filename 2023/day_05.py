from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from tqdm import tqdm


def get_maps(x):
	maps = []
	for line in x:
		maps.append([[s, s+r-1, s-d] for d, s, r in [aoc.ints(l) for l in line.split('\n')[1:]]])

	return maps


def map_values(vals, maps):
	new_v = []
	for v in vals:
		for start, end, diff in maps:
			if start <= v <= end:
				new_v.append(v-diff)
				break
		else:
			new_v.append(v)
	
	return new_v


def map_ranges(ranges, maps):
	new_ranges = []
	while len(ranges) > 0:
		start, end = ranges.pop()

		for a, b, diff in maps:
			if a <= start <= b:  # does the start of the range overlaps a map?
				if end <= b:  # does the end of the range also overlap the map?
					new_ranges.append([start-diff, end-diff])
				else:
					# split range
					new_ranges.append([start-diff, b-diff])
					ranges.append([b+1, end])
				break
			elif a <= end <= b:  # does only the end of the range overlap the map
				# split range
				ranges.append([start, a-1])
				new_ranges.append([a-diff, end-diff])
				break
		else:  # if there is no mapping then keep range
			new_ranges.append([start, end])

	return new_ranges


def part1(x):
	seeds = aoc.ints(x[0])
	maps = get_maps(x[1:])

	for m in maps:
		seeds = map_values(seeds, m)

	return min(seeds)


def part2(x):
	seeds = aoc.ints(x[0])
	maps = get_maps(x[1:])

	ranges = [[seeds[i], seeds[i] + seeds[i+1] - 1] for i in range(0, len(seeds), 2)]

	for m in maps:
		ranges = map_ranges(ranges, m)

	return min(min(ranges))


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