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


def apply_mask(mask, val):
	bin_val = bin(val)[2:].zfill(36)
	new_val = ""

	for m, v in zip(mask, bin_val):
		if m == "X":
			new_val += str(v)
		else:
			new_val += m

	return new_val


def part1(x):
	mem = {}
	mask = None
	for line in x:
		if "mask" in line:
			mask = str(line.split(" = ")[1])
		else:
			addr, val = aoc.ints(line)
			val = apply_mask(mask, val)
			mem[addr] = val

	return sum([int(v, 2) for v in mem.values()])


def decode_addr(mask, addr):
	mask = str(mask)
	bin_val = bin(addr)[2:].zfill(36)
	new_vals = [""]	

	for i in range(len(mask)):
		if mask[i] == "X":
			rep_vals = []
			for bit in ['1', '0']:
				for j in range(len(new_vals)):
					rep_vals.append(new_vals[j] + bit)
			new_vals = rep_vals

		elif mask[i] == '0':
			for j in range(len(new_vals)):
				new_vals[j] += bin_val[i]
		else:
			for j in range(len(new_vals)):
				new_vals[j] += "1"

	new_addrs = []
	for val in new_vals:
		new_addrs.append(int(val, 2))
	
	return new_addrs


def part2(x):
	mem = {}
	mask = None
	for line in x:
		if "mask" in line:
			mask = line.split(" = ")[1]
		else:
			addr, val = aoc.ints(line)
			addrs = decode_addr(mask, addr)
			for add in addrs:
				mem[add] = val

	return sum([v for v in mem.values()])


data = collect_input("input.txt")
#data = collect_input("test_input2.txt")

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