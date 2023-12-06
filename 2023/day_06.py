from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def get_wins(t, d):
	high = math.ceil((-t - math.sqrt(t**2 - 4 * -1 * -d)) / (-2))
	low = math.floor((-t + math.sqrt(t**2 - 4 * -1 * -d)) / (-2))
	
	return (high - 1) - low


def part1(x):
	times = aoc.ints(x[0])
	dists = aoc.ints(x[1])
	return math.prod([get_wins(t, d) for t, d in zip(times, dists)])


def part2(x):
	t = int( ''.join(x[0].split()[1:]) )
	d = int( ''.join(x[1].split()[1:]) )
	return get_wins(t, d)
	

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