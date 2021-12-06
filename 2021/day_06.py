from collections import *
import math
import numpy as np


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def solution(x, days):
	fish = [x.count(i) for i in range(9)]
	for _ in range(days):
		num_reset = fish.pop(0)
		fish[6] += num_reset
		fish.append(num_reset)
	
	return sum(fish)


data = collect_input("input.txt")
data = [int(x) for x in data.split(',')]

# Part 1
print(solution(data.copy(), 80))

# Part 2
print(solution(data.copy(), 256))