from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
import re


def part1(x):
	return sum(math.prod(aoc.ints(ins)) for ins in re.findall(r"mul\(\d+,\d+\)", x))


def part2(x):
	ans = 0
	do = True

	ins_list = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", x)
	
	for ins in ins_list:
		if ins[0] == "m" and do:
			ans += math.prod(aoc.ints(ins))
		else:
			do = (ins == "do()")

	return ans


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

#data = list(map(str, data.split('\n')))

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