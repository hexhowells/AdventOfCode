from collections import *
import math
import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc


def collect_input(filename):
    with open(filename) as inputfile:
        data = inputfile.read()

    return data.rstrip()


def search(grid, row, col, row_acc=0, col_acc=0):
    while grid.valid(row+row_acc, col+col_acc):
        row += row_acc
        col += col_acc
        yield grid[row][col]


def solve(x):
    grid = aoc.Grid(x, cell_type=int)
    best_score = 0
    visible_trees = set()
    
    for (r, c) in grid.all_points():
        score = 1

        # search in all 4 directions from the current tree
        for (r_acc, c_acc) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            line_score = 0
            visible = True  # is the tree visible from outside the grid?

            for tree in search(grid, r, c, r_acc, c_acc):
                line_score += 1
                if tree >= grid[r][c]: 
                    visible = False
                    break

            if visible: visible_trees.add((r,c))
            score *= line_score
                    
        best_score = max(best_score, score)

    return len(visible_trees), best_score


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1 and 2
ans1, ans2 = solve(data.copy())
print(ans1)
if ans1 != "Part 1 Empty": pyperclip.copy(ans1)

print(ans2)
if ans2 != "Part 2 Empty": pyperclip.copy(ans2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))