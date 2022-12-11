from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from operator import add, mul


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


class Monkey:
	def __init__(self):
		self.items = []
		self.operation = None
		self.operation_val = None
		self.test = None
		self.case1 = None
		self.case2 = None


def parse_monkeys(x):
	monkeys = {}
	
	for i, monkey in enumerate(x):
		m = Monkey()

		lines = monkey.split("\n")
		m.items = aoc.ints(lines[1])
		m.op = add if lines[2].split(" ")[-2] == "+" else mul
		m.oprand = lines[2].split(" ")[-1]
		m.test = aoc.ints(lines[3])[0]
		m.case1 = aoc.ints(lines[4])[0]
		m.case2 = aoc.ints(lines[5])[0]

		monkeys[i] = m

	return monkeys


def simulate(monkeys, rounds, func):
	inspected = Counter()

	for _ in range(rounds):
		for i in range(len(monkeys)):
			while monkeys[i].items:
				inspected[i] += 1
				curr_item = monkeys[i].items.pop(0)
				oprand = curr_item if monkeys[i].oprand == "old" else int(monkeys[i].oprand)

				# update stress
				curr_item =  func(monkeys[i].op(curr_item, oprand))
				
				# throw item
				m_idx = monkeys[i].case1 if (curr_item % monkeys[i].test) == 0 else monkeys[i].case2
				monkeys[m_idx].items.append(curr_item)

	return inspected


def part1(x):
	monkeys = parse_monkeys(x)
	inspected = simulate(monkeys, 20, lambda a: a // 3)
	a, b = sorted(inspected.values())[-2:]
	return a * b


def part2(x):
	monkeys = parse_monkeys(x)
	mod_test = math.prod([m.test for m in monkeys.values()])
	inspected = simulate(monkeys, 10_000, lambda a: a % mod_test)
	a, b = sorted(inspected.values())[-2:]
	return a * b


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n\n')))

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