from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def cycle(ticks, strength, register, pixels):
	if register-1 <= ticks%40 <= register+1:
		pixels.append('#')
	else:
		pixels.append('.')
	ticks += 1
	if ticks in [20, 60, 100, 140, 180, 220]: strength += (register * ticks)

	return ticks, strength


def solve(x):
	register, ticks, strength = 1, 0, 0
	pixels = []

	for i, line in enumerate(x):
		if "noop" in line:
			ticks, strength = cycle(ticks, strength, register, pixels)
		else:
			ticks, strength = cycle(ticks, strength, register, pixels)
			ticks, strength = cycle(ticks, strength, register, pixels)
			register += int(line.split(" ")[1])

	print(strength)
	for i in range(0, len(pixels), 40):
		print(''.join(pixels[i:i+40]))


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1 and 2
solve(data)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))