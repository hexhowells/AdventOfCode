from collections import *
import math
from timeit import default_timer as timer
import itertools


def collect_input(filename):
	with open(filename) as inputfile:
		data = inputfile.read()

	return data.rstrip()


def get_scanners(x):
	scanners = []
	for scanner in x:
		beacons = []
		for points in scanner.split("\n")[1:]:
			beacons.append(tuple([int(p) for p in points.split(",")]))
		scanners.append(beacons)
	
	return scanners


def orientations(scanner):
	for x, y, z in itertools.permutations([0,1,2]):
		for sign_x, sign_y, sign_z in itertools.product([-1,1], repeat=3):
			new_scanner = []
			for point in scanner:
				X = point[x]*sign_x
				Y = point[y]*sign_y
				Z = point[z]*sign_z
				new_scanner.append((X,Y,Z))
			yield new_scanner


def get_offsets(ap, sp):
	(ax, ay, az) = ap
	(sx, sy, sz) = sp
	return (ax-sx, ay-sy, az-sz)


def translate_coords(scanner, xo, yo, zo):
	t_beacon = []
	for (x, y, z) in scanner:
		t_beacon.append((x+xo, y+yo, z+zo))
	return t_beacon


def matching_beacons(anchor, scanner):
	matching = 0
	for beacon in scanner:
		if beacon in anchor:
			matching += 1
		if matching >= 12:
			return matching
	return matching
 

def manhattan_dist(a, b):
	return sum([abs(aa-bb) for aa, bb in zip(a, b)])


def largest_dist(sos):
	max_dist = 0
	for so1 in sos:
		for so2 in sos:
			max_dist = max(max_dist, manhattan_dist(so1, so2))
	return max_dist


def get_hashes(points):
	hash_map = {}
	for p in points:
		neighbour_dists = {}
		for np in points:
			if np != p:
				neighbour_dists[np] = manhattan_dist(p, np)
		
		n1, n2 = sorted(neighbour_dists, key=neighbour_dists.get)[:2]
		d1, d2 = neighbour_dists[n1], neighbour_dists[n2]
		dist_hash = (d1 + d2) * manhattan_dist(n1, n2)
		hash_map[dist_hash] = (p, n1, n2)
	
	return hash_map


def matching_beacon_hashes(s_hashes, a_hashes):
	s_beacons = set()
	for s_hash in s_hashes:
		if s_hash in a_hashes:
			[s_beacons.add(b) for b in s_hashes[s_hash]]
	
	return s_beacons


def num_matching_hashes(s_hashes, a_hashes):
	return sum([s_hash in a_hashes for s_hash in s_hashes])


def find_beacon_position(anchor, scanner, anchor_hashes, scanner_hashes):
	if num_matching_hashes(scanner_hashes, anchor_hashes) >= 12:
		indexes = [scanner.index(b) for b in matching_beacon_hashes(scanner_hashes, anchor_hashes)]
		for rot_scanner in orientations(scanner):
			for a_beacon in anchor:
				for idx in indexes:
					s_beacon = rot_scanner[idx]
					xo, yo, zo = get_offsets(a_beacon, s_beacon)
					t_beacons = translate_coords(rot_scanner, xo, yo, zo)
					
					if matching_beacons(anchor, t_beacons) >= 12:
						return True, list(set(anchor + t_beacons)), (xo, yo, zo)
	return False, anchor, (-1,-1,-1)
	

def solutions(x):
	scanners = get_scanners(x)
	Q = deque()
	[Q.append((s, get_hashes(s))) for s in scanners]

	# anchor - original scanner and beacon cluster
	anchor, anchor_hashes = Q.popleft()
	scanner_origins = []
	scanners_left = len(Q)

	while Q:
		if scanners_left != len(Q):
			scanners_left = len(Q)
			print("scanners remaining: {}".format(scanners_left))

		scanner, scanner_hashes = Q.popleft()

		found, anchor, s_origin = find_beacon_position(anchor, scanner, anchor_hashes, scanner_hashes)
		if not found:
			Q.append((scanner, scanner_hashes))
		else:
			scanner_origins.append(s_origin)
			anchor_hashes.update(scanner_hashes)

	
	return len(anchor), largest_dist(scanner_origins)


data = collect_input("input.txt")
data = [x for x in data.split('\n\n')]

start = timer()

part1, part2 = solutions(data)
print("{}\n{}".format(part1, part2))

end = timer()
print("\nTime elapsed: {:.3}s".format(end - start))