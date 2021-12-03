from collections import *
import math

def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def part1(x):
	bit_len = len(x[0])
	ones = [0] * bit_len
	zeros = [0] * bit_len

	for byte in x:
		for i in range(bit_len):
			if byte[i] == "1":
				ones[i] += 1
			else:
				zeros[i] += 1

	gamma = ''.join(["1" if ones[j] > zeros[j] else "0" for j in range(bit_len)])
	gamma = int(gamma, 2)
	epsilon = gamma ^ int("1"*bit_len, 2)
	
	return gamma * epsilon

	

check_oxy = lambda a, b : a >= b
check_c02 = lambda a, b : a < b

def get_ratings(_x, bit_check):
	x = _x.copy()
	bit_len = len(x[0])

	for i in range(bit_len):
		if len(x) == 1: break

		bits = {"0": [], "1": []}
		for j in range(len(x)):
			bits[x[j][i]].append(x[j])
		
		x = bits["1"] if bit_check(len(bits["1"]), len(bits["0"])) else bits["0"]

	return int(x[0], 2)


def part2(x):
	oxy = get_ratings(x, check_oxy)
	c02 = get_ratings(x, check_c02)

	return oxy * c02


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))