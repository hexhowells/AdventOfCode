from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import networkx as nx


def part1(x):
	G = nx.Graph()

	for line in x:
		key, values = line.split(': ')
		[G.add_edge(key, v) for v in values.split(' ')]

	[G.remove_edge(*edge) for edge in nx.minimum_edge_cut(G)]
		
	return math.prod([len(c) for c in nx.connected_components(G)])


def part2(x):
	return "Part 2 Empty"


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

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