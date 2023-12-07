from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import functools


def rank(hand):
	counts = Counter(hand)
	freqs = tuple(sorted(counts.values(), reverse=True))
	match freqs:
		case (5,): return 7
		case (4, 1): return 6
		case (3, 2): return 5
		case (3, 1, 1): return 4
		case (2, 2, 1): return 3
		case (2, 1, 1, 1): return 2
		case _: return 1


def suit(card, p2=False):
	if p2: suits = 'J 2 3 4 5 6 7 8 9 T Q K A'.split(' ')
	else: suits = '2 3 4 5 6 7 8 9 T J Q K A'.split(' ')
	
	return suits.index(card)


def joker(hand):
	if 'J' not in hand: return hand
	if hand.count('J') == 5: return hand

	c = Counter(hand)
	if 'J' in c: del c['J']
	
	return hand.replace('J', c.most_common(1)[0][0])


def compare(p2=False):
	def func(a, b):
		og_h1, og_h2 = a[0], b[0]
		hand1, hand2 = (joker(og_h1), joker(og_h2)) if p2 else (og_h1, og_h2)

		rank_a, rank_b = rank(hand1), rank(hand2)
		if rank_a != rank_b:
			return 1 if rank_a > rank_b else -1

		for c1, c2 in zip(og_h1, og_h2):
			suit_a, suit_b = suit(c1, p2), suit(c2, p2)
			if suit_a != suit_b:
				return 1 if suit_a > suit_b else -1

		return 0

	return func


def solve(x, p2=False):
	key_func = functools.cmp_to_key(compare(p2))
	hands = [[a, int(b)] for line in x for a, b in [line.split(" ")]]

	hands = sorted(hands, key=key_func)
	
	return sum([ (i+1) * r for i, (h, r) in enumerate(hands)])


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = solve(data if type(data) == str else data.copy(), p2=True)
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))