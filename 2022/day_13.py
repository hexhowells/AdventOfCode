from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from functools import cmp_to_key


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def tokenise(p):
	tokens = ""
	brackets = 0

	for token in list(p[1:-1]):
		if token == "[": brackets += 1
		elif token == "]": brackets -= 1
		elif token == "," and brackets == 0: token = "|"
		tokens += token

	return tokens.split("|")


def in_order(p1, p2):
	t1, t2 = tokenise(p1), tokenise(p2)

	for left, right in itertools.zip_longest(t1, t2):
		# check empty
		if not left and not right: return 0
		if not right: return 1
		if not left: return -1

		# compare int to int
		if left.isnumeric() and right.isnumeric():
			left, right = int(left), int(right)
			if right > left: return -1
			if left > right: return 1
			else: continue

		# compare list to list
		if left.isnumeric(): left = f'[{left}]'
		if right.isnumeric(): right = f'[{right}]'
		if (valid := in_order(left, right)) != 0: return valid

	return 0


def part1(x):
	ans = 0
	for i, line in enumerate(x):
		p1, p2 = line.split("\n")
		if in_order(p1, p2) == -1: ans += i+1

	return ans


def part2(x):
	packets = x.split("\n") + ["[[2]]", "[[6]]"]
	packets = sorted(packets, key=cmp_to_key(in_order))

	return (packets.index("[[2]]")+1) * (packets.index("[[6]]")+1)


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

start = timer()

# Part 1
ans1 = part1(data.split("\n\n"))
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data.replace("\n\n", "\n"))
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))