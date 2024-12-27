import unittest
from collections import deque
from aoc import *


class TestUtilityFunctions(unittest.TestCase):

    def test_gen_grid(self):
        self.assertEqual(gen_grid(2, 3, 0), [[0, 0, 0], [0, 0, 0]])
        self.assertEqual(gen_grid(2, 4, '.'), [['.', '.', '.', '.'], ['.', '.', '.', '.']])

    def test_triangle(self):
        self.assertEqual(triangle(5), 15)
        self.assertEqual(triangle(0), 0)
        self.assertEqual(triangle(6), 21)

    def test_tuple_operations(self):
        self.assertEqual(add_tuples((1, 2), (3, 4)), (4, 6))
        self.assertEqual(sub_tuples((5, 7), (2, 3)), (3, 4))
        self.assertEqual(mul_tuples((2, 3), (4, 5)), (8, 15))

    def test_shoelace_formula(self):
        self.assertEqual(shoelace_formula([(0, 0), (4, 0), (4, 3)]), 6)

    def test_picks_theorem(self):
        self.assertEqual(picks_theorem(7, 8), 10.0)

    def test_manhattan_dist(self):
        self.assertEqual(manhattan_dist((1, 2), (4, 6)), 7)

    def test_ints(self):
        self.assertEqual(ints("PO1!-4dmS102##"), [1, -4, 102])
        self.assertEqual(ints("12345"), [12345])
        self.assertEqual(ints("-100", neg=False), [100])
        self.assertEqual(ints("ff-55@df,42dGGG1##", neg=False), [55, 42, 1])

    def test_digits(self):
        self.assertEqual(digits("12345"), [1, 2, 3, 4, 5])
        self.assertEqual(digits("Hex11  4H55"), [1, 1, 4, 5, 5])
        self.assertEqual(digits("-100"), [1, 0, 0])
        self.assertEqual(digits("0000"), [0, 0, 0, 0])
        self.assertEqual(digits("-1AAA0#*   -42rr", neg=True), [-1, 0, -4, 2])
        self.assertEqual(digits("-1-2-345", neg=True), [-1, -2, -3, 4, 5])


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(["123", "456", "789"])

    def test_grid_dimensions(self):
        self.assertEqual(self.grid.height, 3)
        self.assertEqual(self.grid.width, 3)
        self.assertEqual(self.grid.h, 3)
        self.assertEqual(self.grid.w, 3)

    def test_get_neighbour_coords(self):
        self.assertEqual(self.grid.get_neighbour_coords((1, 1)), [(0, 1), (2, 1), (1, 0), (1, 2)])

    def test_get_neighbours(self):
        self.assertEqual(self.grid.get_neighbours((1, 1)), ['2', '8', '4', '6'])

    def test_subgrid(self):
        self.assertEqual(self.grid.subgrid(0, 0, 1, 1), [["1", "2"], ["4", "5"]])

    def test_cells_in_subgrid(self):
        self.assertEqual(list(self.grid.cells_in_subgrid(0, 0, 1, 1)), ["1", "2", "4", "5"])

    def test_count(self):
        self.assertEqual(self.grid.count("1"), 1)

    def test_valid(self):
        self.assertTrue(self.grid.valid(0, 0))
        self.assertFalse(self.grid.valid(3, 3))
        self.assertFalse(self.grid.valid(-1, 2))

    def test_get_set(self):
        self.grid.set((1, 1), "X")
        self.assertEqual(self.grid.get((1, 1)), "X")

    def test_find(self):
        self.grid.set((1, 1), "X")
        self.assertEqual(self.grid.find("X"), [(1, 1)])
        self.grid.set((1, 2), "X")
        self.grid.set((0, 0), "X")
        self.assertEqual(self.grid.find("X"), [(0, 0), (1, 1), (1, 2)])

    def test_transpose(self):
        self.grid.transpose()
        self.assertEqual(str(self.grid), "147\n258\n369")

    def test_rotate_90(self):
        self.grid.rotate_90()
        self.assertEqual(str(self.grid), "741\n852\n963")

    def test_cols(self):
        self.assertEqual(list(self.grid.cols()), [['1','4','7'], ['2','5','8'], ['3','6','9']])

    def test_rows(self):
        self.assertEqual(list(self.grid.rows()), [['1','2','3'], ['4','5','6'], ['7','8','9']])



if __name__ == "__main__":
    unittest.main()
