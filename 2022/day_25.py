from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def snafu_to_dec(snafu):
	dec = 0
	for i, char in enumerate(reversed(list(snafu))):
		pow_val = 5**i
		if char == '-':
			dec += pow_val * -1
		elif char == '=':
			dec += pow_val * -2
		else:
			dec += pow_val * int(char)

	return dec


def dec_to_snafu(dec):
	snafu = ""

	while dec > 0:
		rem = dec % 5

		if rem == 3:
			dec = (dec+2) // 5
			snafu += '='
		elif rem == 4:
			dec = (dec+1) // 5
			snafu += '-'
		else:
			dec = dec // 5
			snafu += str(rem)


	return snafu[::-1]


def part1(x):
	dec_ans = sum([snafu_to_dec(line) for line in x])

	return dec_to_snafu(dec_ans)


def part2(x):
	return "Merry Christmas!"


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

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