from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import copy


def get_cubes(s, e):
	cubes = []

	for i in range(s[0], e[0]+1):
		for j in range(s[1], e[1]+1):
			for k in range(s[2], e[2]+1):
				cubes.append([i, j, k])

	return cubes


def overlap(brick_id, new_brick, bricks):
	for b_id, b in bricks.items():
		if brick_id != b_id:
			for cube in new_brick:
				if cube in b:
					return True
	return False


def drop(brick):
	return [[x,y,z-1] for (x,y,z) in brick]


def lift(brick):
	return [[x,y,z+1] for (x,y,z) in brick]


def lowest_cube(brick):
	return min([z for (x,y,z) in brick])


def supports(brick_id, brick, bricks):
	suporting = set()
	for b_id, b in bricks.items():
		if brick_id != b_id and b_id not in suporting:
			for cube in brick:
				if cube in b:
					suporting.add(b_id)
					break
	return suporting


def count(b_id, supporting):
	return sum(b_id in bricks for bricks in supporting.values())


def count_fallen(brick, stacked_bricks, supported_by):
	fallen = []
	stack = [brick]
	seen = set([brick])

	while stack:
		curr_brick = stack.pop()

		# curr_brick is no longer supporting its above bricks, so remove it as a support
		for v in stacked_bricks[curr_brick]:
			supported_by[v].remove(curr_brick)

		# if any bricks now have 0 supports, they fall
		for k, v in supported_by.items():
			if len(v) == 0 and k not in seen:
				fallen.append(k)
				stack.append(k)
				seen.add(k)

	return len(fallen)


def solve(x):
	bricks = {}

	for i, line in enumerate(x):
		_start, _end = line.split('~')
		start = aoc.ints(_start)
		end = aoc.ints(_end)
		#			   id, cubes
		bricks[i] = get_cubes(start, end)

	moved = True
	while moved:
		moved = False
		for b_id, brick in bricks.items():
			if lowest_cube(brick) > 1:
				new_brick = drop(brick)
				if not overlap(b_id, new_brick, bricks):
					bricks[b_id] = new_brick
					moved = True


	# figure out which bricks are below which
	stacked_bricks = {}
	for b_id, brick in bricks.items():
		stacked_bricks[b_id] = supports(b_id, lift(brick), bricks)

	no_fall = set()
	supporting = {}

	# figure out which bricks are solely supporting which
	for b_id, above_bricks in stacked_bricks.items():
		supporting[b_id] = []

		for above_b in above_bricks:
			if count(above_b, stacked_bricks) == 1:
				supporting[b_id].append(above_b)
				
	
	p1 = sum([len(s) == 0 for s in supporting.values()])

	# get the reverse of supporting
	supported_by = defaultdict(list)
	for base, above in stacked_bricks.items():
		for s in above:
			supported_by[s].append(base)

	
	p2 = sum(count_fallen(b_id, stacked_bricks, copy.deepcopy(supported_by)) for b_id in bricks.keys())

	return p1, p2


data = aoc.collect_input("input.txt")
data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1 & Part 2
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))