from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import re


def move_block(blocks, ptr, block_id, num_blocks):
	for i in range(ptr):
		space, num_spaces = blocks[i]

		if space == '.' and (rem := num_spaces - num_blocks) >= 0:
			blocks[i] = (block_id, num_blocks)
			blocks.insert(ptr, ('.', num_blocks))

			if rem > 0: blocks.insert(i+1, ('.', rem))
			
			return True, ptr+1

	return False, ptr


def get_blocks(nums):
	blocks = []

	for i, n in enumerate(nums):
		if (i % 2 == 0):
			blocks.append((i//2, n))
		elif n > 0:
			blocks.append(('.', n))

	return blocks


def part1(x):
	nums = aoc.digits(x[0])
	blocks = []

	for i, n in enumerate(nums):
		blocks += ([i//2] if (i%2==0) else ['.']) * n

	ptr = len(blocks)-1
	for i in range(len(blocks)):
		if ptr <= i: break

		if blocks[i] != '.': continue

		while blocks[ptr] == '.': ptr -= 1

		blocks[i], blocks[ptr] = blocks[ptr], '.'

	return sum([i*n for i, n in enumerate(blocks) if n != '.'])


def part2(x):
	nums = aoc.digits(x[0])
	
	blocks = get_blocks(nums)

	ptr = len(blocks) - 1
	moved = False

	while ptr > 0:
		moved = False

		block_id, num_blocks = blocks.pop(ptr)

		if block_id != '.':
			moved, ptr = move_block(blocks, ptr, block_id, num_blocks)

			if not moved: blocks.insert(ptr, (block_id, num_blocks)) 
		else:
			blocks.insert(ptr, (block_id, num_blocks))
		
		ptr -= 1

	ans, pos = 0, 0
	for (block_id, num_blocks) in blocks:
		if block_id != '.':
			ans += block_id * sum(range(pos, num_blocks+pos))
		pos += num_blocks

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