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


def solve1(name, mem):
	if isinstance(mem[name][0], int):
		return mem[name][0]

	num1, op, num2 = mem[name]
	return eval(f'{solve1(num1, mem)} {op} {solve1(num2, mem)}')


def solve(name, mem, yell, part2=True):
	if isinstance(mem[name][0], int):
		if part1 and name == 'humn':
			return yell
		else:
			return mem[name][0]

	num1, op, num2 = mem[name]
	return int( eval(f'{solve(num1, mem, yell, part2)} {op} {solve(num2, mem, yell, part2)}') )


def part1(x):
	mem = {}
	stack = []
	op_stack = []
	for line in x:
		name, params = line.split(': ')
		params = params.split(" ")
		if params[0].isnumeric():
			mem[name] = [int(params[0])]
		else:
			mem[name] = params

	num1, op, num2 = mem["root"]

	return eval(f'{solve1(num1, mem)} {op} {solve1(num2, mem)}')


def find_start(num1, tar, mem, start, acc, op):
	yell = start
	prev = yell

	while True:
		ans1 = solve(num1, mem, yell)
		if ans1 == tar:
			return True, yell
		if (ans1 - tar) < 0:
			return False, prev

		prev = yell
		yell = eval(f'{yell} {op} {acc}')



def part2(x):
	mem = {}
	stack = []
	op_stack = []
	for line in x:
		name, params = line.split(': ')
		params = params.split(" ")
		if params[0].isnumeric():
			mem[name] = [int(params[0])]
		else:
			mem[name] = params

	num1, op, num2 = mem["root"]

	target = solve(num2, mem, 0)
	_, start = find_start(num1, target, mem, 1, 10, "*")
	zeros = len(str(start)) - 3
	acc = int("1" + ("0" * zeros))
	acc = max(10, acc)
	prev_start = start
	sub = 3

	while True:
		#print("Trying start ", start, acc)
		found, start = find_start(num1, target, mem, start, acc, "+")
		
		if found: return start

		if start == prev_start:
			sub += 1

		zeros = len(str(start)) - sub
		acc = int("1" + ("0" * zeros))
		acc = max(1, acc)

		prev_start = start


	return -1


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