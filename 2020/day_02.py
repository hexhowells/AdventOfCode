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


def part1(x):
	valid = 0

	for policy in x:
		minc, maxc, char, password = policy.replace("-", " ").replace(":", "").split(" ")
		if int(minc) <= password.count(char) <= int(maxc):
			valid += 1

	return valid


def part2(x):
	valid = 0

	for policy in x:
		pos1, pos2, char, password = policy.replace("-", " ").replace(":", "").split(" ")
		if (password[int(pos1)-1] == char) ^ (password[int(pos2)-1] == char):
			valid += 1

	return valid


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = [x for x in data.split('\n')]
#data = [int(x) for x in data.split('\n')]

start = timer()

# Part 1
ans1 = part1(data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))