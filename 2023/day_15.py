from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import functools
import pyperclip
import aoc


def hash_str(s):
	return functools.reduce(lambda v, c: (v + ord(c)) * 17 % 256, s, 0)


def in_box(box, label):
	return any(b[0] == label for b in box)


def del_label(box, label):
	return [b for b in box if b[0] != label]


def mod_box(box, label, val):
	return [(label, val) if b[0] == label else b for b in box]


def part1(x):
	return sum([hash_str(line) for line in x])


def part2(x):
	boxes = defaultdict(list)

	for line in x:
		if '-' in line:
			label, _ = line.split('-')
			boxes[hash_str(label)] = del_label(boxes[hash_str(label)], label)
		else:
			label, val = line.split('=')
			if in_box(boxes[hash_str(label)], label):
				boxes[hash_str(label)] = mod_box(boxes[hash_str(label)], label, int(val))
			else:
				boxes[hash_str(label)].append((label, int(val)))

	return sum((1+k) * (i+1) * v for k, b in boxes.items() for i, (_, v) in enumerate(b))


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split(',')))

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