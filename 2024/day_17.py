from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
from tqdm import tqdm
import pyperclip
import aoc


# def run_small(program, A):
# 	out = []
# 	while A != 0:
# 		B = A % 8
# 		B = B ^ 3
# 		C = A >> B
# 		B = B ^ C
# 		B = B ^ 3
# 		A = A >> 3
# 		out.append(B % 8)

# 	return out


def get_combo(oprand, registers):
	match oprand:
		case 0 | 1 | 2 | 3:
			return oprand
		case 4:
			return registers['A']
		case 5:
			return registers['B']
		case 6:
			return registers['C']
		case 7:
			print("Invalid combo operand")


def run_ins(opcode, oprand, ptr, registers):
	jmp = False
	output = None

	if opcode not in [1, 3, 4]:
		oprand = get_combo(oprand, registers)

	match opcode:
		case 0:
			registers['A'] = int(registers['A'] / (2**oprand))
		case 1:
			registers['B'] = registers['B'] ^ oprand
		case 2:
			registers['B'] = oprand % 8
		case 3:
			if registers['A'] != 0:
				ptr = oprand
				jmp = True
		case 4:
			registers['B'] = registers['B'] ^ registers['C']
		case 5:
			output = oprand % 8
		case 6:
			registers['B'] = int(registers['A'] / (2**oprand))
		case 7:
			registers['C'] = int(registers['A'] / (2**oprand))

	if not jmp:
		ptr += 2

	return ptr, registers, output



def run(program, A):
	registers = {'A':A, 'B':0, 'C':0}
	ptr = 0

	outputs = []

	while ptr < len(program)-1:
		opcode, oprand = program[ptr], program[ptr+1]
		ptr, registers, output = run_ins(opcode, oprand, ptr, registers)

		if output is not None:
			outputs.append(output)

	return outputs


def part1(x):
	A_reg = aoc.ints(x[0])[0]
	program = aoc.ints(x[1])

	return ','.join(map(str, run(program, A_reg)))


def part2(x):
	program = aoc.ints(x[1])

	stack = [(a, 0) for a in range(8)]
	
	while stack:
		A, idx = stack.pop()

		output = run(program, A)

		if output[-(idx+1)] != program[-(idx+1)]:
			continue

		if idx == len(program) - 1:
			return A
		
		for next_A in range(8):
			num = f'{A:03b}{next_A:03b}'
			stack.append( (int(num, 2), idx + 1) )



data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input2.txt")

data = list(map(str, data.split('\n\n')))

start = timer()

# Part 1
ans1 = part1(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data if type(data) == str else data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))