from collections import *
import math
#import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


seen = {}

def run(modules, vals, mem, cycle=None):
	# 		         reciver, pulse, sender
	stack = deque([('broadcaster', 0, "button")])
	# keeps track of all high and low signals sent
	sent = Counter()

	while stack:
		recv, pulse, sender = stack.popleft()
		sent[pulse] += 1 

		# if one of the NAND gates connecting 'rx' just sent a HIGH, record which cycle it happened
		if (pulse == 1) and (sender in ['sx', 'jt', 'kb', 'ks']) and (sender not in seen):
			seen[sender] = cycle

		# ignore signals from output or rx
		if recv == 'output' or recv not in modules: continue

		m_type, outputs = modules[recv]

		match m_type:
			case "b":
				# broadcast pulse to all recievers
				for out in outputs: stack.append((out, pulse, recv))

			case "%":
				# ignore if pulse is 1
				if pulse == 1: continue
				# flip if pulse is 0
				vals[recv] = 1 - vals[recv]
				# broadcast new pulse to all recievers
				for out in outputs: stack.append((out, vals[recv], recv))

			case "&":
				# update memory
				mem[recv][sender] = pulse

				# get output pulse
				p = 1 - all(mem[recv].values())

				# broadcase pulse to all recievers
				for out in outputs: stack.append((out, p, recv))

	return sent, modules, vals, mem


def get_dicts(x):
	modules = {}

	for line in x:
		name, outputs = line.replace('broadcaster', 'bbroadcaster').split(' -> ')
		modules[name[1:]] = (name[0], outputs.split(', '))

	vals = {}
	mem = defaultdict(dict)
	for sender in modules.keys():
		vals[sender] = 0

		# if module <sender> is a NAND gate, create memories for each possible input
		if modules[sender][0] == '&':
			for _sender, out in modules.items():
				# if module <_sender> sends signals to the NAND gate <sender> create a memory for it
				if sender in out[1]:
					mem[sender][_sender] = 0

	return modules, vals, mem



def part1(x):
	modules, vals, mem = get_dicts(x)
	
	h, l = 0, 0

	for _ in range(1000):
		sent, modules, vals, mem = run(modules, vals, mem)
		h += sent[1]
		l += sent[0]

	return h * l


def part2(x):
	modules, vals, mem = get_dicts(x)

	for i in range(1_000_000_000):
		sent, modules, vals, mem = run(modules, vals, mem, cycle=i+1)
		interest = [vals[k] for k in ['sx', 'jt', 'kb', 'ks']]
		
		# once every NAND module of interest has sent a HIGH signal
		# calculate when their HIGH signals will align
		if len(seen) == 4:
			return math.lcm(*list(seen.values()))


data = aoc.collect_input("input.txt")
#data = aoc.collect_input("test_input2.txt")

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