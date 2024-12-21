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


pair_map = {
	">>": ["AA"],
	"<<": ["AA"],
	"^^": ["AA"],
	"vv": ["AA"],
	"AA": ["AA"],
	
	"A^": ["A<","<A"],
	"A<": ["Av","v<","<<","<A"],
	"Av": ["A<","<v","vA"],
	"A>": ["Av","vA"],
	
	"^A": ["A>",">A"],
	"^<": ["Av","v<","<A"],
	"^>": ["Av", "v>", ">A"],
	
	"v>": ["A>",">A"],
	"v<": ["A<","<A"],
	"vA": ["A^","^>",">A"],
	
	">v": ["A<","<A"],
	">A": ["A^","^A"],
	">^": ["A<","<^","^A"],

	"<A": ["A>",">>",">^","^A"],
	"<v": ["A>",">A"],
	"<^": ["A>",">^","^A"],


    "A3": ["A^","^A"],
	"38": ["A<","<^","^^","^A"],
	"82": ["Av","vv","vA"],
	"2A": ["Av","v>",">A"],
	"A1": ["A^","^<","<<","<A"],
	"17": ["A^","^^","^A"],
	"76": ["Av","v>",">>",">A"], 
	"6A": ["Av","vv","vA"],
	"A4": ["A^","^^","^<","<<","<A"],
	"46": ["A>",">>",">A"],
	"63": ["Av","vA"],
	"3A": ["Av","vA"],
	"A0": ["A<","<A"],
	"08": ["A^","^^","^^","^A"],
	"83": ["Av","vv","v>",">A"], 
	"A7": ["A^","^^","^^","^<","<<","<A"],  
	"78": ["A>",">A"],
	"89": ["A>",">A"],
	"9A": ["Av","vv","vv","vA"],

	# to make the example work
	"02": ["A^","^A"],
	"29": ["A>",">^", "^^", "^A"],
	"A9": ["A^", "^^", "^^", "^A"], 
	"98": ["A<", "<A"],
	"80": ["Av", "vv", "vv", "vA"], 
	"0A": ["A>", ">A"],
	"79": ["A>", ">>", ">A"],
	"45": ["A>", ">A"],
	"56": ["A>", ">A"],
	"37": ["A<", "<<", "<^", "^^", "^A"], 
}



def get_counts(counts):
	new_counts = Counter()

	for k, v in counts.items():
		for p in pair_map[k]:
			new_counts[p] += v

	return new_counts


def solve(x):
	ans = 0
	p1, p2 = 0, 0

	for line in x:
		num_code = aoc.ints(line)
		seq = ['A'] + [x for x in line]
		
		counts = Counter()
		for a, b in zip(seq, seq[1:]):
			hash_str = f'{a}{b}'
			for p in pair_map[hash_str]:
				counts[p] += 1

		all_counts = [counts]
		for i in range(25):
			all_counts.append(get_counts(all_counts[i]))
		
		p1 += num_code[0] * sum([v for v in all_counts[2].values()])
		p2 += num_code[0] * sum([v for v in all_counts[25].values()])

	return p1, p2


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

# Part 2
#ans2 = part2(data if type(data) == str else data.copy())
print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))