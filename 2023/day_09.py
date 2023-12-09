from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


get_diff = lambda h: [h[i+1] - h[i] for i in range(0, len(h)-1)]
	

def predict(histories, p2=False):
	predicted_val = 0
	for line in reversed(histories):
		if p2:
			predicted_val = line[0] - predicted_val
		else:
			predicted_val = line[-1] + predicted_val

	return predicted_val


def solve(x):
	p1, p2 = 0, 0
	for line in x:
		histories = [aoc.ints(line)]

		while True:
			new_h = get_diff(histories[-1])

			if sum(new_h) == 0:
				p1 += predict(histories)
				p2 += predict(histories, p2=True)
				break
			
			histories.append(new_h)

	return p1, p2


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1
ans1, ans2 = solve(data if type(data) == str else data.copy())
print(ans1)
print(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))