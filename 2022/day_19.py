from collections import *
import math
# import numpy as np
from timeit import default_timer as timer
import itertools
import pyperclip
import aoc
from tqdm import tqdm


def collect_input(filename):
    with open(filename) as inputfile:
        data = inputfile.read()

    return data.rstrip()


def simulate(blueprint, mins):
    best = {}

    # ore, clay, obsidian, geodes, ore_robot, clay_robot, obsidian_robot, geode_robot, time
    q = deque([(0, 0, 0, 0, 1, 0, 0, 0, mins)])
    seen = {}

    # unpack blueprint
    ore_cost = blueprint[0]
    clay_cost = blueprint[1]
    obsidian_ore_cost = blueprint[2]
    obsidian_clay_cost = blueprint[3]
    geode_ore_cost = blueprint[4]
    geode_obsidian_cost = blueprint[5]

    # most amount of ore we could spend in one turn
    max_ore_spend = max([ore_cost, clay_cost, obsidian_ore_cost, geode_ore_cost])

    while q:
        ore, clay, obsidian, geode, ore_r, clay_r, obsidian_r, geode_r, t = q.popleft()

        # keet track of most geodes collected for every minute
        best_key = mins - t
        best[best_key] = geode if (best_key not in best) else max(best[mins-t], geode)

        # terminate branch if time runs out
        if t == 0: continue

        # only need as many robots as max_spend
        ore_r =      min(ore_r,      max_ore_spend)
        clay_r =     min(clay_r,     obsidian_clay_cost)
        obsidian_r = min(obsidian_r, geode_obsidian_cost)

        # cap max amount of material minded after robot cap
        ore =      min( ore,      t * max_ore_spend       - ore_r      * (t-1) )
        clay =     min( clay,     t * obsidian_clay_cost  - clay_r     * (t-1) )
        obsidian = min( obsidian, t * geode_obsidian_cost - obsidian_r * (t-1) )

        state = (ore, clay, obsidian, geode, ore_r, clay_r, obsidian_r, geode_r)

        # terminate branch if already explored
        if (state in seen) and (t <= seen[state]): continue
        seen[state] = t

        # store material quantities before mining more
        prev_ore, prev_clay, prev_obsidian = ore, clay, obsidian

        # add state where we just mine ore and buy no more robots
        state = (ore+ore_r, clay+clay_r, obsidian+obsidian_r, geode+geode_r, ore_r, clay_r, obsidian_r, geode_r, t-1)
        ore, clay, obsidian, geode, ore_r, clay_r, obsidian_r, geode_r, t = state
        q.append(state)

        # add states where we buy robots
        if prev_ore >= ore_cost:  # buy ore robot
            q.append((ore-ore_cost, clay, obsidian, geode, ore_r+1, clay_r, obsidian_r, geode_r, t))
        if prev_ore >= clay_cost:  # buy clay robot
            q.append((ore-clay_cost, clay, obsidian, geode, ore_r, clay_r+1, obsidian_r, geode_r, t))
        if (prev_ore >= obsidian_ore_cost) and (prev_clay >= obsidian_clay_cost):  # buy obsidian robot
            q.append((ore-obsidian_ore_cost, clay-obsidian_clay_cost, obsidian, geode, ore_r, clay_r, obsidian_r+1, geode_r, t))
        if (prev_ore >= geode_ore_cost) and (prev_obsidian >= geode_obsidian_cost):  # buy geode robot
            q.append((ore-geode_ore_cost, clay, obsidian-geode_obsidian_cost, geode, ore_r, clay_r, obsidian_r, geode_r+1, t))

    return best


# for each blueprint find best geode
#   for each minute perform every possible action and add to queue
#     do above until time runs out, return most geodes found for all branches
def solve(x):
    blueprints = [aoc.ints(b)[1:] for b in x]

    part1, part2 = 0, 1
    for i, blueprint in tqdm(enumerate(blueprints), total=len(blueprints)):
        limit = 32 if i<3 else 24
        geodes = simulate(blueprint, limit)
        part1 += geodes[24] * (i+1)
        if i < 3:
            part2 *= geodes[32]

    return part1, part2


data = collect_input("input.txt")
#data = collect_input("test_input.txt")

data = list(map(str, data.split('\n')))

start = timer()

# Part 1 and 2
p1, p2 = solve(data.copy())
print(p1)
print(p2)

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))
