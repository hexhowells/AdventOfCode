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


def mix(numbers, epochs):
	num_len = len(numbers)
	for epoch in range(epochs):
		#print(f'On round {epoch} of mixing')
		for i in range(num_len):
			new_idx = (numbers[i][0] + numbers[i][1]) % (num_len-1)
			if new_idx == 0: new_idx = num_len - 1

			for j in range(num_len):
				if numbers[i][0] < numbers[j][0] <= new_idx: numbers[j][0] -= 1
				if numbers[i][0] > numbers[j][0] >= new_idx: numbers[j][0] += 1
				
			numbers[i][0] = new_idx


	start = sum([numbers[k][0] if numbers[k][1] == 0 else 0 for k in range(num_len)])
	positions = [( (val+start) % num_len) for val in [1000, 2000, 3000]]
	ans = sum([numbers[i][1] if numbers[i][0] in positions else 0 for i in range(num_len)])

	return ans


def part1(x):
	numbers = [[i, int(a)] for i, a in enumerate(x)]
	return mix(numbers, 1)


def part2(x):
	numbers = [[i, int(a)*811589153] for i, a in enumerate(x)]
	return mix(numbers, 10)


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

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