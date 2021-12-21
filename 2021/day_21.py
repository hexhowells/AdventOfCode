from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_start_pos(x):
	a = x[0].split(": ")[1]
	b = x[1].split(": ")[1]
	return int(a)-1, int(b)-1


def part1(x):
	p1, p2 = get_start_pos(x)
	s1 = s2 = 0
	die = 0
	
	while True:
		r1 = die*3 + 6
		die += 3
		p1 = (p1 + r1) % 10
		s1 += p1+1
		if s1 >= 1000: break

		r2 = die*3 + 6
		die += 3
		p2 = (p2 + r2) % 10
		s2 += p2+1
		if s2 >= 1000: break

	return min(s1, s2) * die


mem = {}
def get_scores(game_state):
	p1, p2, s1, s2 = game_state
	if s1 >= 21: return (1, 0)
	if s2 >= 21: return (0, 1)
	if (game_state) in mem: return mem[(game_state)]

	total_scores = (0,0)

	for die in itertools.product([1,2,3], repeat=3):
		new_p1 = (p1 + sum(die)) % 10
		new_s1 = s1 + new_p1 + 1

		acc_s1, acc_s2 = get_scores((p2, new_p1, s2, new_s1))
		total_scores = (total_scores[0] + acc_s2, total_scores[1] + acc_s1)
	
	mem[(game_state)] = total_scores

	return total_scores


def part2(x):
	p1, p2 = get_start_pos(x)
	return max(get_scores((p1, p2, 0, 0)))


data = collect_input("input.txt")
data = [x for x in data.split('\n')]

start = timer()

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))