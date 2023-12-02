from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def valid(games):
	lim = {'red': 12, 'blue': 14, 'green': 13}
	for game in games:
		for c in game.split(', '):
			if aoc.ints(c)[0] > lim[c.split(' ')[1]]: 
				return False

	return True


def part1(x):
	ans = 0

	for line in x:
		_game_id, games = line.split(': ')
		game_id = aoc.ints(_game_id)[0]
		
		if valid(games.split('; ')):
			ans += game_id

	return ans


def power(games):
	cubes = {'red': [], 'green': [], 'blue': []}
	for game in games:
		for c in game.split(', '):
			cubes[c.split(' ')[1]].append(aoc.ints(c)[0])
	
	return math.prod([max(v) for v in cubes.values()])


def part2(x):
	ans = 0

	for line in x:
		_game_id, games = line.split(': ')
		game_id = aoc.ints(_game_id)[0]
		ans += power(games.split('; '))

	return ans


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