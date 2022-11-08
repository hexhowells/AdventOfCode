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


def contains_shiny_gold(mem, bag):
	if bag.name == "shiny gold bag": return True

	if bag.name in mem:
		for val in mem[bag[1]]:
			valid = contains_shiny_gold(mem, val)
			if valid:
				return valid

	return False


def get_count(mem, bag):
	if bag.name in mem:
		count = sum( [(get_count(mem, inner_bag) * bag.quantity) for inner_bag in mem[bag.name]] )
		count += bag.quantity
		return count
	
	return bag.quantity
	

def construct_bag_graph(x):
	mem = {}
	Bag = namedtuple('Bag', 'quantity, name')
	for line in x:
		root, rules = line.split(" contain ")
		rules = rules.replace('.','').split(", ")
		root = root.replace('bags', 'bag')

		
		if rules[0] == "no other bags":
			continue
		mem[root] = []
		for rule in rules:
			quan, bag = int(rule[0]), rule[2:]
			bag = bag.replace('bags', 'bag')
			mem[root].append(Bag(quan, bag))

	return mem


def part1(x):
	ans = 0
	mem = construct_bag_graph(x)

	for k, v in mem.items():
		for val in v:
			if contains_shiny_gold(mem, val):
				ans += 1
				break

	return ans


def part2(x):
	mem = construct_bag_graph(x)
	ans = sum([get_count(mem, val) for val in mem['shiny gold bag']])

	return ans


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