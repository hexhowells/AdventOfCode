from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


add = lambda a, b: a + b
mul = lambda a, b: a * b
pipe = lambda a, b: int(str(a) + str(b))


def compute(nums, ops):
	acc = nums[0]

	for i, op in enumerate(ops):
		acc = op(acc, nums[i+1])

	return acc


def check(test_value, ops, symbols):
	for combo in itertools.product(symbols, repeat=len(ops) - 1):
		if compute(ops, combo) == test_value:
			return True

	return False


def solve(x):
	p1, p2 = 0, 0

	for line in x:
		test_value, *ops = aoc.ints(line)
		
		if check(test_value, ops, [add, mul]):
			p1 += test_value
			p2 += test_value
		elif check(test_value, ops, [add, mul, pipe]):
			p2 += test_value

	return p1, p2


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1 & 2
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))