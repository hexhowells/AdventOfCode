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


def get_changes(s):
	changes = []
	secrets = [s]
	prev = 0
	for _ in range(2000):
		s = (s ^ (s * 64)) % 16777216
		s = (s ^ (s // 32)) % 16777216
		s = (s ^ (s * 2048)) % 16777216
		s_temp = int(str(s)[-1])
		changes.append(s_temp-prev)
		secrets.append(s_temp)
		prev = s_temp

	return changes[1:], secrets[1:]


# updates scores counter with each n=4 sequence and it's price
def update_scores(changes, secrets, scores):
	seen = set()

	for i, window in enumerate(zip(changes, changes[1:], changes[2:], changes[3:])):
		if window not in seen:
			seen.add(window)
			scores[window] += secrets[i+4]


def part1(x):
	ans = 0

	secrets = [int(n) for n in x]

	for _ in range(2000):
		new_secrets = []
		for s in secrets:
			s = (s ^ (s*64)) % 16777216
			s = (s ^ (s // 32)) % 16777216
			s = (s ^ (s * 2048)) % 16777216
			new_secrets.append(s)

		secrets = new_secrets

	return sum(secrets)


def part2(x):
	_secrets = [int(n) for n in x]

	changes, secrets = [], []
	for s in _secrets:
		chg, sec = get_changes(s)
		changes.append(chg)
		secrets.append(sec)
	
	scores = Counter()
	for c, s in zip(changes, secrets):
		update_scores(c, s, scores)

	return max(scores.values())


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