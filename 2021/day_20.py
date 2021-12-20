from collections import *
import math
import numpy as np
from timeit import default_timer as timer


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def show_image(image):
	conv = {1: '#', 0:'.'}
	for line in image.tolist():
		print(''.join([conv[c] for c in line]))


def bin_to_int(binary):
  num = 0
  for b in binary:
    num = (2 * num) + b
  return num


def windows(image, size):
	for i in range(size):
		for j in range(size):
			yield image[i:i+3, j:j+3], (i, j)


def enhance(image, algorithm, step):
	image = np.pad(image, 2, constant_values=(step%2!=0))

	size = image.shape[0] - 2
	new_image = np.full((size, size), 0)

	for w, (i, j) in windows(image, size):
		w = w.flatten().tolist()
		new_image[i, j] = algorithm[bin_to_int(w)]

	return new_image
		

def solutions(x, steps):
	conv = {'#': 1, '.': 0}
	algorithm = [conv[c] for c in list(x[0])]
	image = np.asarray([[conv[c] for c in list(r)] for r in x[1].split("\n")])

	for step in range(steps):
		image = enhance(image, algorithm, step)
		
	return np.count_nonzero(image == 1)


data = collect_input("input.txt")
data = [x for x in data.split('\n\n')]

start = timer()

# Part 1
print(solutions(data.copy(), 2))

# Part 2
print(solutions(data.copy(), 50))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))