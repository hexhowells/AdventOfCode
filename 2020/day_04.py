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
	ans = 0
	for passport in x:
		valid_fields = [f in passport for f in 'byr: iyr: eyr: hgt: hcl: ecl: pid:'.split(" ")]
		if sum(valid_fields) >= 7: ans += 1

	return ans


def part2(x):
	ans = 0
	for passport in x:
		passport = passport.replace('\n', " ")
		passport_fields = passport.split(" ")
		valid = 0
		for entry in passport_fields:
			f, val = entry.split(":")

			if f == 'byr':
				if 1920 <= int(val) <= 2002: valid += 1
			elif f == 'iyr':
				if 2010 <= int(val) <= 2020: valid += 1
			elif f == 'eyr':
				if 2020 <= int(val) <= 2030: valid += 1
			elif f == 'hgt':
				if 'cm' in val:
					if 150 <= int(val.replace('cm', '')) <= 193: valid += 1
				elif 'in' in val:
					if 59 <= int(val.replace('in', '')) <= 76: valid += 1
			elif f == 'hcl':
				if val[0] == '#' and len(val[1:]) == 6:
					v = [True if a in '0123456789abcdef' else False for a in val[1:]]
					if sum(v) == len(v):
						valid += 1
			elif f == 'ecl':
				if val in 'amb blu brn gry grn hzl oth': valid += 1
			elif f == 'pid':
				if len(val) == 9: valid += 1

		if valid >= 7:
			ans += 1

	return ans


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = [x for x in data.split('\n\n')]
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