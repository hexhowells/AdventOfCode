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


def part1(x):
	ans = 0
	for line in x:
		jolts = list(map(int, list(line)))
		digit_1 = jolts.index(max(jolts[:-1]))
		digit_2 = jolts.index(max(jolts[digit_1+1:]))
		j = int(f'{jolts[digit_1]}{jolts[digit_2]}')
		ans += j
	return ans


def part2(x):
	ans = 0
	for line in x:
		jolts = list(map(int, list(line)))

		j = ""
		start = 0
		for i in range(11, -1, -1):
			j_idx = jolts.index(max(jolts[start:len(jolts)-i]), start)
			j += str(jolts[j_idx])
			start = j_idx+1

		ans += int(j)
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