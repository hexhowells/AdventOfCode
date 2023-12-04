from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


points = lambda w, n: sum([nn in w for nn in n])
get_card = lambda line: [aoc.ints(a) for a in line.replace(':', '|').split('|')]


def part1(x):
	ans = 0

	for line in x:
		card, winners, nums = get_card(line)
		s = points(winners, nums)
		ans += (s>0) * (2**(s-1))

	return int(ans)


def get_num_cards(scratchcards, card, mem):
	ans = 1
	if card in mem: return mem[card]
	
	if (s:= points(*scratchcards[card])) > 0:
		ans += sum(get_num_cards(scratchcards, card+i, mem) for i in range(1, s+1))

	mem[card] = ans

	return ans


def part2(x):
	ans = 0
	scratchcards = {}
	mem = {}

	for line in x:
		card, winners, nums = get_card(line)
		scratchcards[card[0]] = (winners, nums)

	for card, (winners, nums) in scratchcards.items():
		if (s:= points(winners, nums)) > 0:
			ans += sum(get_num_cards(scratchcards, card+i, mem) for i in range(1, s+1))

	return ans + len(x)


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