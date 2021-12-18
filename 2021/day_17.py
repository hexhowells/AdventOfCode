from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import re


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


data = collect_input("input.txt")
values = re.findall(r'[-\d]+', data)
x_min, x_max, y_min, y_max = [int(v) for v in values]


def within_target(x_vel, y_vel):
	highest_y = 0
	x = y = 0

	while True:
		x += x_vel
		y += y_vel

		y_vel -= 1
		if x_vel > 0: x_vel -= 1

		if y > highest_y: highest_y = y

		if y < y_min or x > x_max: break

		if x_min <= x and x <= x_max and y_min <= y and y <= y_max:
			return True, highest_y


	return False, -1


def solutions(x):
	num_valid = 0
	best_y = 0
	for x_vel in range(0, 250):
		for y_vel in range(-250, 250):
			valid, highest_y = within_target(x_vel, y_vel)

			if valid:
				num_valid += 1

				if highest_y > best_y: best_y = highest_y

	return best_y, num_valid



start = timer()

part1, part2 = solutions(data)
print("{}\n{}".format(part1, part2))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))