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


def part1(x):
	ans = 0
	for line in x:
		id1, id2 = aoc.ints(line, neg=False)
		for id_num in range(id1, id2+1):
			nid_str = str(id_num)
			half = len(nid_str) // 2
			if nid_str[:half] == nid_str[half:]: 
				ans += id_num
	
	return ans


def even_divisors(n: int):
    return [d for d in range(1, n//2+1) if n % d == 0]


def repeating(str, num):
	for i in range(num, len(str), num):
		if str[:num] != str[i:num+i]: 
			return False
	
	return True


def part2(x):
	ans = 0
	for line in x:
		id1, id2 = aoc.ints(line, neg=False)
		for id_num in range(id1, id2+1):
			id_str = str(id_num)

			divisors = even_divisors(len(id_str))

			for div in divisors:
				if repeating(id_str, div):
					ans += id_num
					break
	return ans


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split(',')))

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