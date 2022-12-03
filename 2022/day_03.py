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
	alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	ans = 0

	for line in x:
		a, b = line[:len(line)//2], line[len(line)//2:]
		sim = set(a) & set(b)

		ans += sum([alph.index(ch)+1 for ch in sim])

	return ans


def part2(x):
	alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	ans = 0
	buf = []
	
	for i in range(3, len(x)+1, 3):
		buf = x[i-3:i]

		a, b, c = buf[0], buf[1], buf[2]
		sim = set()
		sim = set(a) & set(b) & set(c)
		
		ans += sum([alph.index(ch)+1 for ch in sim])

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