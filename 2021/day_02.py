from collections import *
import math

def collect_input():
	with open("input.txt") as inputfile:
		data = inputfile.read()

	return data.rstrip()


def part1(x):
	hor, depth = 0, 0

	for raw in x:
		move, num = raw.split(" ")
		num = int(num)
		if move == "forward":
			hor += num
		elif move == "up":
			depth -= num
		elif move == "down":
			depth += num

	return depth * hor


def part2(x):
	hor, depth, aim = 0, 0, 0

	for raw in x:
		move, num = raw.split(" ")
		num = int(num)
		if move == "forward":
			hor += num
			depth += aim * num
		elif move == "up":
			aim -= num
		elif move == "down":
			aim += num

	return depth * hor


data = collect_input()
data = [x for x in data.split('\n')]

# Part 1
print(part1(data.copy()))

# Part 2
print(part2(data.copy()))