from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from z3 import Int, Solver, sat


def intersection(m1, c1, m2, c2):
	x = (c2 - c1) / (m1 - m2)
	y = (m1 * x) + c1

	return x, y


def in_past(x, y, new_x, new_y, x_vel, y_vel):
	return ((x - new_x > 0) == (x_vel > 0)) and ((y - new_y > 0) == (y_vel > 0))


def part1(x):
	lines = []

	for line in x:
		x, y, z, x_vel, y_vel, z_vel = aoc.ints(line)
		m = ((y + y_vel) - y) / ((x + x_vel) - x)  # slope
		c = y - (m * x)  # y-intercept
		lines.append((x, y, x_vel, y_vel, m, c))

	min_lim = 200000000000000
	max_lim = 400000000000000

	ans = 0

	for i in range(len(lines)):
		for j in range(i+1, len(lines)):
			x1, y1, x_vel1, y_vel1, m1, c1 = lines[i]
			x2, y2, x_vel2, y_vel2, m2, c2 = lines[j]

			if m1 == m2: continue  # lines are parallel so will never cross

			x, y = intersection(m1, c1, m2, c2)

			past1 = in_past(x1, y1, x, y, x_vel1, y_vel1)
			past2 = in_past(x2, y2, x, y, x_vel2, y_vel2)

			if (min_lim <= x <= max_lim) and (min_lim <= y <= max_lim) and not (past1 or past2):
				ans += 1

	return ans


def part2(x):
	lines = []

	for line in x:
		x, y, z, x_vel, y_vel, z_vel = aoc.ints(line)
		lines.append((x,y,z,x_vel,y_vel,z_vel))

	# define optimiser
	opt = Solver()

	# define unknowns to be found (starting position and velocity)
	sx, sy, sz = Int('sx'), Int('sy'), Int('sz')
	sx_vel, sy_vel, sz_vel = Int('sx_vel'), Int('sy_vel'), Int('sz_vel')

	# for each piece of hail, add its pos and vel to the solver
	for i, (x, y, z, x_vel, y_vel, z_vel) in enumerate(lines):
		t = Int(f't{i}') # time of collision will be different for each hail

		opt.add(x + x_vel * t == sx + sx_vel * t)
		opt.add(y + y_vel * t == sy + sy_vel * t)
		opt.add(z + z_vel * t == sz + sz_vel * t)

	# insure a solution can be found
	assert opt.check() == sat, "Solution not found!"

	return sum(opt.model()[a].as_long() for a in [sx, sy, sz])


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