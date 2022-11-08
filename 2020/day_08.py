from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import copy


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def execute(lines):
	line_count = len(lines)
	p = 0
	acc = 0
	mem = set()

	while p < line_count:
		if p in mem: return True, acc
		mem.add(p)

		opcode, oprand = lines[p]
		incr_p = 1

		if opcode == "acc":
			acc += oprand
		elif opcode == "jmp":
			incr_p = oprand

		p += incr_p
	
	return False, acc


def parse_instructions(x):
	lines = []
	for line in x:
		opcode, oprand = line.split(" ")
		oprand = int(oprand)
		lines.append([opcode, oprand])
	return lines


def part1(x):
	lines = parse_instructions(x)
	_, acc = execute(lines)

	return acc


def part2(x):
	lines = parse_instructions(x)
	swap = {'jmp':'nop', 'nop':'jmp'}

	for i, line in enumerate(lines):
		if line[0] == 'acc': continue

		new_lines = copy.deepcopy(lines)
		new_lines[i][0] = swap[new_lines[i][0]]

		loop, acc = execute(new_lines)
		if not loop:
			return acc


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