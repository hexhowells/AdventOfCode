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


# check if piece collides with wall or a placed piece
def collision(point, piece, placed):
	for acc in piece:
		p = (point[0]+acc[0], point[1]+acc[1])
		if (p[0] in placed and p[1] in placed[p[0]]) or (p[1] < 0) or (p[1] > 6) or p[0] <= 0:
			return True
		
	return False


# add all segments of piece to placed dict
def place_piece(point, piece, placed):
	for acc in piece:
		new_point = (point[0]+acc[0], point[1]+acc[1])
		if new_point[0] in placed:
			placed[new_point[0]].append(new_point[1])
		else:
			placed[new_point[0]] = [new_point[1]]



def simulate(x, part1):
	# given the coords of the bottom left corner as reference, where do the blocks for each piece go?
	piece_map = {
			0: [(0, 0), (0, 1), (0, 2), (0, 3)],
			1: [(0, 1), (1, 0), (1, 1), (2, 1), (1, 2)],
			2: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
			3: [(0, 0), (1, 0), (2, 0), (3, 0)],
			4: [(0, 0), (0, 1), (1, 0), (1, 1)]
			}
	piece_height = {0:1, 1:3, 2:3, 3:4, 4:2}
	action = {'>':1, '<':-1}

	load_new_piece = True
	number_placed = 0
	height = 0
	curr_piece_idx = -1

	# coords of all rock segments placed, key is the row, value is all cols for that row
	placed = {}

	# how many rocks have been placed for each height
	rocks_height = {}

	point = (0, 0)

	# used for wrapping around when moves runs out
	move_idx = -1
	move_mod = len(x)

	while True:
		move_idx += 1

		# spawn new piece in starting location
		if load_new_piece:
			curr_piece_idx = (curr_piece_idx + 1) % 5
			piece = piece_map[curr_piece_idx]
			point = (height+4, 2)
			load_new_piece = False

		# move piece horizontally
		next_point = (point[0], point[1] + action[x[move_idx % move_mod]])
		if not collision(next_point, piece, placed):
			point = next_point

		# drop piece vertically
		drop_piece = (point[0]-1, point[1])
		if not collision(drop_piece, piece, placed):
			point = drop_piece
		# place piece to rest
		else:
			place_piece(point, piece, placed)
			number_placed += 1
			load_new_piece = True
			height = max(height, (point[0] + piece_height[curr_piece_idx])-1)
			
			rocks_height[height] = number_placed

			if part1 and number_placed == 2022: return height
			if not part1:
				pattern_found, pattern_start_height = find_pattern(placed)
				if pattern_found:
					# this is horrible... but it works
					# essentially finds where a pattern starts and ends
					# need to figure out the height of the inital blocks (before a pattern starts)
					# then how many patterns can be placed until we go over the piece limit
					# after the piece limit is reached, there are still some blocks left to place
					# then calculate the height after those blocks get placed (using info from the pattern)
					pattern_height = height - pattern_start_height - 20
					num_start_rocks = rocks_height[pattern_start_height]
					num_pattern_rocks = rocks_height[height-20]-num_start_rocks
					num_patterns_seen = (1000000000000 - num_start_rocks) // num_pattern_rocks
					added_rocks = ((1000000000000 - num_start_rocks) % num_pattern_rocks)
					rocks_goal = added_rocks + rocks_height[pattern_start_height]
					added_height = 0
					for k, v in rocks_height.items():
						if v == rocks_goal:
							added_height = k-pattern_start_height
							break

					# ans = height of starting random blocks
					#     + number of patterns we can repeat until block limit reached
					#     * the height of the pattern
					#     + the height after the half-pattern is placed (to reach to block limit)
					return pattern_start_height + (num_patterns_seen * pattern_height) + added_height


# creates a hash of a segment of the board
def get_hash(placed, start, height):
	hash_str = ""
	for i in range(start, start+height):
		hash_str += ''.join(list(map(str, placed[i])))
	
	return hash_str


# finds if a hash of the top 20 rows exists somewhere else in the board
def find_pattern(placed):
	h = len(placed)
	if h < 3000: return False, -1  # dont check until n rows have pieces

	seg_size = 20
	search_hash = get_hash(placed, h-seg_size, seg_size)

	for i in range(1, h-seg_size*2):
		if search_hash == get_hash(placed, i, seg_size): return True, i

	return False, -1
		

def part1(x):
	return simulate(x, part1=True)


def part2(x):
	return simulate(x, part1=False)
	


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(data)

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