import random
import unittest
from parameterized import parameterized

from src.solutions.BruteForceSolution import BruteForceSolution
from src.solutions.PointsSolution import PointsSolution
from src.solutions.Solution import Solution
from src.solutions.models.Square import Square
from src.data.random_generator.random_problem import generate_problem


def random_brute_force_problem():
    random.seed(51)
    square, points = generate_problem(5, 5, 7)
    return points, square, BruteForceSolution(square, points).compute_solution()


brute_force_cases = [
    [
        {(1, 1), (3, 3)},
        Square(0, 4, 0, 4),
        [Square(0, 4, 0, 3), Square(1, 4, 0, 4), Square(0, 4, 1, 4), Square(0, 3, 0, 4)]
    ],
    random_brute_force_problem(),
    random_brute_force_problem(),
    random_brute_force_problem(),
    [
        set(),
        Square(0, 4, 0, 4),
        []
    ],
    [{(1, 1)}, Square(0, 4, 0, 4), [Square(0, 4, 0, 4)]],
]

test_cases = [
    *brute_force_cases,
    [
        {(13, 1), (1, 22), (15, 23), (16, 9), (9, 21), (12, 5), (5, 15), (17, 22), (8, 18), (12, 16)},
        Square(0, 20, 0, 24),
        [Square(0, 16, 1, 15)]
    ],
]


class MyTestCase(unittest.TestCase):
    @parameterized.expand(brute_force_cases)
    def _test_brute_force_resolver(self, points, square, solution):
        # given
        resolver = BruteForceSolution(square.copy(), points)

        # when
        computed_solution = resolver.compute_solution()

        # then
        self.assertCountEqual(computed_solution, solution)

    @parameterized.expand(test_cases)
    def _test_border_resolver(self, points, square, solution):
        # given
        resolver = Solution(square.copy(), points)

        # when
        computed_solution = resolver.compute_solution()

        # then
        self.assertCountEqual(computed_solution, solution)

    @parameterized.expand(test_cases)
    def test_points_resolver(self, points, square, solution):
        # given
        resolver = PointsSolution(square.copy(), points)

        # when
        computed_solution = resolver.compute_solution()

        # then
        self.assertCountEqual(computed_solution, solution)


if __name__ == '__main__':
    unittest.main()
