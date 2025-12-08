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
import networkx as nx


def euclidean_distance_3d(p1, p2):
	return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)


def solve(x):
	x = [aoc.ints(c) for c in x]
	
	g = nx.Graph()
	g.add_nodes_from([i for i in range(len(x))])

	cons = []
	seen = set()

	for i in range(len(x)):
		for j in range(len(x)):
			if i != j:
				key = str(sorted([i, j]))
				if key not in seen:
					d = euclidean_distance_3d(x[i], x[j])
					cons.append((d, i, j))
					seen.add(key)					
				
	cons = sorted(cons, key=lambda x: x[0])
	edges = [(a, b) for (_, a, b) in cons]

	p1, p2 = 0, 0

	for i, (n1, n2) in enumerate(edges):
		g.add_edge(n1, n2)

		# part 1
		if i == 1000:
			components = list(nx.connected_components(g))
			components = sorted(components, key=len, reverse=True)

			p1 = math.prod([len(c) for c in components[:3]])

		# part 2
		if nx.is_connected(g):
			p2 = x[n1][0] * x[n2][0]
			break
	
	return p1, p2
	

data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))