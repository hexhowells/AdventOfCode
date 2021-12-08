from collections import *
import math
import numpy as np


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def parse_data(x):
	for line in x:
		in_digits, out_digits = line.split(' | ')
		yield  in_digits.split(' '), out_digits.split(' ')


def part1(x):
	ans = 0
	for _, out_digits in parse_data(x):
		ans += sum([len(digit) in [2,3,4,7] for digit in out_digits])

	return ans


seg_to_dec = {
		"abcefg": '0',
		"cf": '1',
		"acdeg": '2',
		"acdfg": '3',
		"bcdf": '4',
		"abdfg": '5',
		"abdefg": '6',
		"acf": '7',
		"abcdefg": '8',
		"abcdfg": '9'
		}


wire_to_seg = lambda segments, seg_map: ''.join(sorted([seg_map[char] for char in segments]))


def decode_segments(in_digits):
	four_seq = [digit for digit in in_digits if len(digit) == 4][0]

	letters = list(''.join(in_digits))
	freqs = {}
	for letter in set(letters):
		freqs[letter] = letters.count(letter)

	seg_map = {}
	for k, v in freqs.items():
		if v == 6:
			seg_map[k] = "b"
		elif v == 4:
			seg_map[k] = "e"
		elif v == 9:
			seg_map[k] = "f"
		elif v == 8:
			if k in four_seq:
				seg_map[k] = "c"
			else:
				seg_map[k] = "a"
		elif v == 7:
			if k in four_seq:
				seg_map[k] = "d"
			else:
				seg_map[k] = "g"
	
	return seg_map

	
def part2(x):
	ans = 0
	for in_digits, out_digits in parse_data(x):
		seg_map = decode_segments(in_digits)
		ans += int(''.join([seg_to_dec[wire_to_seg(digit, seg_map)] for digit in out_digits]))

	return ans


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))