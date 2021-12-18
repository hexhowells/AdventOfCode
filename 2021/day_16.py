from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


ops = [sum, math.prod, min, max,
      lambda vals: vals[0], 
      lambda vals: 1 if vals[0] > vals[1] else 0,
      lambda vals: 1 if vals[0] < vals[1] else 0,
      lambda vals: 1 if vals[0] == vals[1] else 0]


def solutions(bit_seq, p):
	total_version = int( bit_seq[p:p+3], 2)
	type_id = int( bit_seq[p+3:p+6], 2)
	p += 6

	if type_id == 4:
		bin_num = ""
		while True:
			bin_num += bit_seq[p+1: p+5]
			p += 5
			if bit_seq[p-5] == '0':
				break
		
		values = [int(bin_num, 2)]
	else:
		values = []
		header = bit_seq[p]
		p += 1
		if header == '0':
			p_lim = p + 15 + int(bit_seq[p: p+15], 2)
			p += 15
			while p < p_lim:
				p, version, v = solutions(bit_seq, p)
				total_version += version
				values.append(v)
		else:
			num_subs = int(bit_seq[p:p+11], 2)
			p += 11
			for _ in range(num_subs):
				p, version, v = solutions(bit_seq, p)
				total_version += version
				values.append(v)

	return p, total_version, ops[type_id](values)


data = collect_input("input.txt")
data = bin(int('1'+data, 16))[3:]


start = timer()

_, part1, part2 = solutions(data, 0)
print("{}\n{}".format(part1, part2))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))