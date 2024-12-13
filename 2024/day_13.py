from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
from tqdm import tqdm
import pyperclip
import aoc
from z3 import Solver, Int, sat


def solve(ax, ay, bx, by, px, py):
	a_pushes = Int('a_pushes')
	b_pushes = Int('b_pushes')	

	solver = Solver()
	
	eq1 = (ax * a_pushes) + (bx * b_pushes) == px
	eq2 = (ay * a_pushes) + (by * b_pushes) == py
	
	solver.add(eq1, eq2)
	
	if solver.check() == sat:
		solution = solver.model()
		return solution[a_pushes].as_long(), solution[b_pushes].as_long() 
	
	return 0, 0


def part1(x):
	ans = 0

	for line in x:
		ax, ay, bx, by, px, py = aoc.ints(line)

		ans_a, ans_b = solve(ax, ay, bx, by, px, py)
		ans += ans_a*3 + ans_b

	return ans


def part2(x):
	ans = 0

	for line in x:
		ax, ay, bx, by, px, py = aoc.ints(line)

		ans_a, ans_b = solve(ax, ay, bx, by, 10000000000000+px, 10000000000000+py)
		ans += ans_a*3 + ans_b

	return ans


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