from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import copy


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


class Seats(aoc.Grid):
	def see(self, r, c):
		count = 0
		for incr in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
			rr, cc = r+incr[0], c+incr[1]
			
			while self.valid(rr, cc):
				if self.grid[rr][cc] == '#': count += 1
				if self.grid[rr][cc] != '.': break

				rr += incr[0]
				cc += incr[1]

		return count


def solve(seats, occ_func, lim):
	while True:
		new_seats = copy.deepcopy(seats)
		for r, c in seats.all_points():
			seat = seats[r][c]
			occ = occ_func(seats, r, c)

			if seat == "L" and occ == 0:
				new_seats[r][c] = '#'
			elif seat == '#' and occ >= lim:
				new_seats[r][c] = 'L'

		if seats.grid == new_seats.grid: break

		seats = new_seats

	return seats.count('#')


def part1(x):
	seats = aoc.Grid(x)
	return solve(seats, lambda seats, r, c : seats.get_neighbours((r, c), True).count('#'), 4)


def part2(x):
	seats = Seats(x)
	return solve(seats, lambda seats, r, c : seats.see(r, c), 5)
	


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = [x for x in data.split('\n')]
#data = [int(x) for x in data.split('\n')]

start = timer()

#Part 1
ans1 = part1(data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
ans2 = part2(data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))