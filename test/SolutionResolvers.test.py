import random
import unittest
from parameterized import parameterized

from src.BruteForceSolution import BruteForceSolution
from src.PointsSolution import PointsSolution
from src.Solution import Solution
from src.models.Square import Square
from src.random_generator.random_problem import generate_problem


def random_brute_force_problem():
    random.seed(51)
    points = generate_problem(5, 5, 7)
    square = Square(0, 5, 0, 5)
    return points, square, BruteForceSolution(square, points).compute_solution()


test_cases = [
    [
        {(1, 1), (3, 3)},
        Square(0, 4, 0, 4),
        [Square(0, 4, 0, 3), Square(1, 4, 0, 4), Square(0, 4, 1, 4), Square(0, 3, 0, 4)]
    ],
    # [
    #     {(1, 1), (2, 1), (4, 2), (3, 3), (4, 4), (2, 4), (1, 4), },
    #     Square(0, 5, 0, 5),
    #     []
    # ],
    [
        set(),
        Square(0, 4, 0, 4),
        []
    ],
    random_brute_force_problem(),
    random_brute_force_problem(),
    random_brute_force_problem(),
    [{(1, 1)}, Square(0, 4, 0, 4), [Square(0, 4, 0, 4)]],
]


class MyTestCase(unittest.TestCase):
    @parameterized.expand(test_cases)
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
