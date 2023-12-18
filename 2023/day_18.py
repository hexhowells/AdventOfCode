from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def get_coords(ins):
	count = 0
	p = (0,0)
	coords = [p]

	for d, v in ins:
		match d:
			case 'U': p = (p[0]-v, p[1])
			case 'D': p = (p[0]+v, p[1])
			case 'L': p = (p[0], p[1]-v)
			case 'R': p = (p[0], p[1]+v)
		coords.append(p)
		count += v

	return coords, count


def part1(x):
	ins = [(line[0], int(line[2:4])) for line in x]
		
	coords, count = get_coords(ins)

	return aoc.shoelace_formula(coords) + (count // 2) + 1
		

def part2(x):
	conv = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
	ins = [ (conv[line[-2]], int(line[-7:-2], 16)) for line in x]
		
	coords, count = get_coords(ins)

	return aoc.shoelace_formula(coords) + (count // 2) + 1


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