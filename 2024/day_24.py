from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
from functools import cache
import heapq
from tqdm import tqdm
import pyperclip
import aoc
from graphviz import Digraph


def create_graph(tuples_list):
	graph = Digraph(format='png')

	z_nodes, x_nodes, y_nodes = set(), set(), set()

	for a, op, b, d in tuples_list:
		graph.node(a, label=a)
		graph.node(b, label=b)
		graph.node(d, label=d)

		graph.edge(a, d, label=op)
		graph.edge(b, d, label=op)

		# collect input and output nodes
		if d.startswith('z'):
			z_nodes.add(d)

		if a.startswith('x'):
			x_nodes.add(a)
		if b.startswith('x'):
			x_nodes.add(b)

		if a.startswith('y'):
			y_nodes.add(a)
		if b.startswith('y'):
			y_nodes.add(b)

	# create a subgraph to align input and output nodes
	if z_nodes:
		with graph.subgraph() as s:
			s.attr(rank='same')
			for node in z_nodes:
				s.node(node)

	if x_nodes:
		with graph.subgraph() as s:
			s.attr(rank='same')
			for node in x_nodes:
				s.node(node)

	if y_nodes:
		with graph.subgraph() as s:
			s.attr(rank='same')
			for node in y_nodes:
				s.node(node)

	return graph


def part1(x):
	reg = {}
	ins = deque([])

	for r in x[0].split('\n'):
		key, val = r.split(': ')
		reg[key] = int(val)

	for l in x[1].split('\n'):
		a, op, b, d = l.replace("-> ", '').split(' ')
		ins.append((a, op, b, d))

	while ins:
		a, op, b, d = ins.popleft()

		if a not in reg or b not in reg:
			ins.append((a, op, b, d))
			continue

		if op == "AND":
			reg[d] = reg[a] & reg[b]
		elif op == 'XOR':
			reg[d] = reg[a] ^ reg[b]
		elif op == 'OR':
			reg[d] = reg[a] | reg[b]


	binary_str = ''.join([str(reg[k]) for k in sorted(reg.keys(), reverse=True) if k[0] == 'z'])

	return int(binary_str, 2)


def part2(x):
	reg = {}
	ins = deque([])

	for r in x[0].split('\n'):
		key, val = r.split(': ')
		reg[key] = int(val)

	swap = {
	'vcg': 'z24', 
	'z24': 'vcg',
	'z09': 'rkf',
	'rkf': 'z09',
	'z20': 'jgb',
	'jgb': 'z20',
	'rrs': 'rvc',
	'rvc': 'rrs',
	}

	for l in x[1].split('\n'):
		a, op, b, d = l.replace("-> ", '').split(' ')
		d = swap[d] if d in swap else d
		ins.append((a, op, b, d))

	graph = create_graph(ins)	
	graph.render("graph", view=True)
	
	return ','.join(sorted(swap.keys()))


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