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
import pulp


lmap = {'.': '#', '#': '.'}
def push_button(lights, button):
	for b in button: lights[b] = lmap[lights[b]]

	return lights


def part1(x):
	ans = 0

	for line in x:
		pattern, *_buttons, _ = line.split(' ')
		pattern = list(pattern[1:-1])
		buttons = [aoc.ints(b) for b in _buttons]
		lights = ['.'] * len(pattern)

		q = deque([(lights.copy(), b, 1) for b in buttons])
		seen = set()

		while True:
			l, b, c = q.popleft()

			l = push_button(l, b)
			l_hash = tuple(l)
			if l_hash in seen: continue
			seen.add(l_hash)

			if l == pattern:
				ans += c
				break
			
			for b in buttons: 
				q.append((l.copy(), b, c+1))
	
	return ans


"""
Can formalise the problem as an integer linear programming problem and solve with pulp
--

(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
(3)		[0, 0, 0, 1] = A
(1,3)	[0, 1, 0, 1] = B
(2)		[0, 0, 1, 0] = C
(2,3)	[0, 0, 1, 1] = D
(0,2)	[1, 0, 1, 0] = E
(0,1)	[1, 1, 0, 0] = F
{3,5,4,7}  [3, 5, 4, 7] = S

Constraints
--
A*a + B*b + C*c + D*d + E*e + F*f = S
  A[0]*a + B[0]*b + C[0]*c + D[0]*d + E[0]*e + F[0]*f = S[0]
  A[1]*a + B[1]*b + C[1]*c + D[1]*d + E[1]*e + F[1]*f = S[1]
  A[2]*a + B[2]*b + C[2]*c + D[2]*d + E[2]*e + F[2]*f = S[2]
  A[3]*a + B[3]*b + C[3]*c + D[3]*d + E[3]*e + F[3]*f = S[3]

Minimise [a + b + c + d + e + f]
"""
def part2(x):
	ans = 0

	for line in x:
		_, *buttons, jolts = line.split(' ')
		buttons = [aoc.ints(b) for b in buttons]
		jolts = aoc.ints(jolts)

		coeffs = [[0] * len(jolts) for _ in range(len(buttons))]

		for i in range(len(buttons)):
			for b in buttons[i]: coeffs[i][b] = 1
		
		model = pulp.LpProblem("day10", pulp.LpMinimize)
		vars = [pulp.LpVariable(str(i), lowBound=0, cat="Integer") for i in range(len(buttons))]

		for i in range(len(jolts)):
			model += pulp.lpSum([coeffs[j][i] * vars[j] for j in range(len(buttons))]) == jolts[i]
		
		model += pulp.lpSum(vars)  # minimise the sum of vars
		model.solve(pulp.PULP_CBC_CMD(msg=False))

		ans += sum([int(var.value()) for var in vars])
	
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