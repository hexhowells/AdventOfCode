from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from functools import cache
from tqdm import tqdm


@cache
def blink(stone, depth, lim):
	if depth == lim:
		return 1

	if stone == 0:
		return blink(1, depth+1, lim)
	elif len(str(stone)) % 2 == 0:
		stone_str = str(stone)
		split = len(stone_str) // 2
		return blink(int(stone_str[:split]), depth+1, lim) + blink(int(stone_str[split:]), depth+1, lim)
	else:
		return blink((stone * 2024), depth+1, lim)


def part1(x):
	stones = aoc.ints(x[0])
	return sum([blink(s, 0, 25) for s in stones])


def part2(x):
	stones = aoc.ints(x[0])
	return sum([blink(s, 0, 75) for s in stones])
	

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