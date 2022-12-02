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
	win = {"A": "Y", "B": "Z", "C": "X"}
	draw = {"A": "X", "B": "Y", "C":"Z"}
	score = {"X": 1, "Y": 2, "Z": 3}

	ans = 0
	for line in x:
		a, b = line.split(" ")
		if win[a] == b:
			ans += score[b] + 6
		elif draw[a] == b:
			ans += score[b] + 3
		else:
			ans += score[b] 

	return ans


def part2(x):
	win = {"A": "Y", "B": "Z", "C": "X"}
	draw = {"A": "X", "B": "Y", "C":"Z"}
	lose = {"A": "Z", "B": "X", "C":"Y"}
	score = {"X": 1, "Y": 2, "Z": 3}

	ans = 0
	for line in x:
		a, b = line.split(" ")
		if b == "X":
			ans += score[lose[a]] 
		elif b == "Y":
			ans += score[draw[a]] + 3
		else:
			ans += score[win[a]] + 6

	return ans


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

#data = [x for x in data.split('\n\n')]
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