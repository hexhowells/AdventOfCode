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


# R = current clique
# P = candidate vertices to be added to R
# X = set of verticies already processed


def find_triangles(r, p, x, graph, triangles):
	if len(r) == 3:
		triangles.append(r)

	for v in list(p):
		find_triangles(r | {v}, p & graph[v], x & graph[v], graph, triangles)
		p.remove(v)
		x.add(v)


def bron_kerbosch(r, p, x, graph):
	maximal_cliques = []

	if not p and not x:
		maximal_cliques.append(r)

	for v in list(p):
		maximal_cliques.extend( 
			bron_kerbosch(r | {v}, p & graph[v], x & graph[v], graph) 
			)
		p.remove(v)
		x.add(v)

	return maximal_cliques


def make_graph(edges):
	graph = defaultdict(set)
	for (a, b) in edges:
		graph[a].add(b)
		graph[b].add(a)

	return graph


def part1(x):
	edges = [n.split('-') for n in x]
	graph = make_graph(edges)
	
	triangles = []
	find_triangles(set(), set(graph.keys()), set(), graph, triangles)

	return sum(1 for t in triangles if any(n[0] == 't' for n in t))


def part2(x):
	edges = [n.split('-') for n in x]
	graph = make_graph(edges)
			
	largest_clique = list(max(bron_kerbosch(set(), set(graph.keys()), set(), graph), key=len))

	return ','.join(sorted(largest_clique))
	

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