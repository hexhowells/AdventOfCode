from collections import *
from timeit import default_timer as timer
import networkx as nx


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def create_graph(x):
	graph = nx.Graph()
	for line in x:
		(a, b) = line.split("-")
		if b == "start" or a == "end":
			graph.add_edge(b, a)
		else:
			graph.add_edge(a, b)

	return graph


def DFS(graph, stack, small_caves, lim):
	current_cave = stack.pop()
	if current_cave == "end":
		if max(small_caves.values()) > 0:
			return 1
	
	paths = 0
	for cave in graph.neighbors(current_cave):
		if cave.islower():
			if small_caves[cave] >= 1 and max(small_caves.values()) >= lim:
				continue

		if cave != "start":
			stack.append(cave)
			if cave.islower(): small_caves[cave] += 1
			paths += DFS(graph, stack, small_caves, lim)
			if cave.islower(): small_caves[cave] -= 1

	return paths


data = collect_input("input.txt")
data = [x for x in data.split('\n')]
graph = create_graph(data)

start = timer()

# Part 1
print(DFS(graph, ["start"], Counter(), 1))

# Part 2
print(DFS(graph, ["start"], Counter(), 2))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))