from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


Axis = namedtuple("Axis", "low high")

def parse_input(x):
	global Axis
	for line in x:
		state, coords = line.split(" ")
		axis = []
		for ax in coords.split(","):
			ax_low, ax_high = [int(a) for a in ax[2:].split("..")]
			axis.append(Axis(ax_low, ax_high))

		yield state, tuple(axis)


def intersect_axis(ax1, ax2):
	global Axis
	if ax2.low > ax1.high or ax1.low > ax2.high:
		return None

	i_low = max(ax1.low, ax2.low)
	i_high = min(ax1.high, ax2.high)
	return Axis(i_low, i_high)


def intersection(b1, b2):
	x1, y1, z1 = b1
	x2, y2, z2 = b2

	x = intersect_axis(x1, x2)
	y = intersect_axis(y1, y2)
	z = intersect_axis(z1, z2)

	if None in [x, y, z]:
		return None
	else:
		return (x, y, z)


class Cuboid:
	def __init__(self, bounds):
		self.bounds = bounds
		self.voids = []

	def remove(self, bounds):
		void_bounds = intersection(self.bounds, bounds)
		if not void_bounds:
			return

		for void in self.voids:
			void.remove(void_bounds)

		self.voids.append(Cuboid(void_bounds))
		

	def volume(self):
		cuboid_volume = math.prod([(ax.high - ax.low + 1) for ax in self.bounds])
		voids_volume = sum([void.volume() for void in self.voids])
		return cuboid_volume - voids_volume


def in_init_area(bounds):
	for ax in bounds:
		if ax.low < -50 or ax.high > 50:
			return False
	return True


def part1(x):
	cuboids = []
	for state, bounds in parse_input(x):
		if in_init_area(bounds):
			for cuboid in cuboids:
				cuboid.remove(bounds)
			if state == "on":
				cuboids.append(Cuboid(bounds))

	return sum([cuboid.volume() for cuboid in cuboids])


def part2(x):
	cuboids = []
	for state, bounds in parse_input(x):
		for cuboid in cuboids:
			cuboid.remove(bounds)
		if state == "on":
			cuboids.append(Cuboid(bounds))

	return sum([cuboid.volume() for cuboid in cuboids])


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))