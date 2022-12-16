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


def floyd_warshall(nV, grid):
	distance = list(map(  lambda i: list(map(lambda j: j, i)), grid  ))

	for k in range(nV):
		for i in range(nV):
			for j in range(nV):
				distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
	return distance


INF = 1_000_000

def build_grid(paths, flows, v2i, i2v):
	grid = []
	for i in range(len(paths)):
		row = []
		for j in range(len(paths)):
			if i == j:
				row.append(0)
			elif i2v[j] in paths[i2v[i]]:
				row.append(1)
			else:
				row.append(INF)
		grid.append(row)
	return grid


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

x = list(map(str, data.split('\n')))


paths, flows = {}, {}
v2i, i2v = {}, {}
idx = 0

interest = []

#
# Process input
#
for line in x:
	tokens = line.split(" ")
	valve = tokens[1]
	flow = aoc.ints(tokens[4])[0]
	path = line.replace("to valves", "to valve").split("to valve ")[1].split(", ")

	flows[valve] = flow
	paths[valve] = path
	if flow > 0: interest.append(valve)

	if valve not in v2i:
		v2i[valve] = idx
		i2v[idx] = valve
		idx += 1


def DFS(path, to_visit, depth):
	for next_v in to_visit:
		if next_v in path: continue

		new_depth = (depth - dist[ v2i[path[-1]] ][ v2i[next_v] ])
		if new_depth <= 0: continue

		score = (flows[next_v] * new_depth) + mem[''.join(path)]
		
		path.append(next_v)
		mem[''.join(path)] = score

		if new_depth <= 0: return 0

		DFS(path.copy(), to_visit.copy(), new_depth-1)
		path.pop()



start = timer()

#
# find shortest paths between each node pair
#
grid = build_grid(paths, flows, v2i, i2v)
dist = floyd_warshall(len(paths), grid)

#
# Part 1
#
mem = {"AA":0}
DFS(["AA"], interest, 29)
pressure = sorted(mem.values(), reverse=True)[0]
valve_path = max(mem, key=mem.get)
print(f'{pressure}\n{valve_path}\n')


#
# Part 2
#
mem = {"AA":0}
DFS(["AA"], interest, 25)
pressure = sorted(mem.values(), reverse=True)[0]
valve_path = max(mem, key=mem.get)


_mem_paths = list(filter(lambda x: len(x) > 2, list(mem.keys())))

def str_to_int(path):
	new_path = []
	for i in range(0, len(path)-1, 2):
		v = path[i:i+2]
		new_path.append(v2i[v])

	return new_path


mem_paths = [str_to_int(x) for x in _mem_paths]
scores = {}

table_a = {}
table_b = {}

# there are many paths that contain the same valves (just in different orders)
# out of these we only want to keep the path that has the highest score
# this greatly prunes the search space (5mins -> 5secs)
for a, b in zip(_mem_paths, mem_paths):
	hash_val = ''.join(list(map(str, set(b))))
	
	if hash_val in scores:
		if mem[a] > scores[hash_val]:
			scores[hash_val] = mem[a]
			table_a[hash_val] = a
			table_b[hash_val] = b
	else:
		scores[hash_val] = mem[a]
		table_a[hash_val] = a
		table_b[hash_val] = b


path_strings = []
path_indexes = []

for k in table_a.keys():
	path_strings.append(table_a[k])
	path_indexes.append(table_b[k])


best = 0
best_pair = ""
for i in range(len(path_indexes)):
	path1 = path_indexes[i][1:]
	path1_set = set(path1)

	for j in range(i, len(path_indexes)):
		path2 = path_indexes[j][1:]

		if path1_set.isdisjoint(path2): # if they dont share common elements
			if (cache:=mem[path_strings[i]]+mem[path_strings[j]]) > best:
				best = cache
				best_pair = path_strings[i] + " " + path_strings[j]

print(best)
print(best_pair)


end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))
