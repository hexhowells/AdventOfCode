from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_pair_rules(lines):
	pairs = {}
	for line in lines.split("\n"):
		(a, b) = line.split(" -> ")
		pairs[a] = b
	return pairs


def solutions(x, n):
	seq = list(x[0])
	pair_rules = get_pair_rules(x[1])

	quantities = Counter()
	for i in range(2, len(seq)+1):
		quantities[''.join(seq[i-2:i])] += 1

	for step in range(n):
		q = Counter()
		for k, v in quantities.items():
			p = pair_rules[k]
			q[k[0]+p] += v
			q[p + k[1]] += v

		quantities = q

	freqs = Counter()
	for k, v in quantities.items():
		freqs[k[0]] += v
	freqs[seq[-1]] += 1

	return max(freqs.values()) - min(freqs.values())
		

data = collect_input("input.txt")
data = [x for x in data.split('\n\n')]

start = timer()

# Part 1
print(solutions(data.copy(), 10))

# Part 2
print(solutions(data.copy(), 40))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))