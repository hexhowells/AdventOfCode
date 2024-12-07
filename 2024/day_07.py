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


def check(seq, ops, ans):
	if len(seq) == 1: return seq[0] == ans

	if seq[0] > ans: return False

	for op in ops:
		a, b, *rest = seq
		if check([op(a, b)] + rest, ops, ans):
			return True

	return False


def solve(x):
	p1, p2 = 0, 0

	for line in x:
		test_value, *nums = aoc.ints(line)
		
		if check(nums, [add, mul], test_value):
			p1 += test_value
			p2 += test_value
		elif check(nums, [add, mul, pipe], test_value):
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