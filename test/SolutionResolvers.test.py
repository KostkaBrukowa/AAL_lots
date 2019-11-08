import unittest
from parameterized import parameterized

from src.BruteForceSolution import BruteForceSolution
from src.PointsSolution import PointsSolution
from src.Solution import Solution
from src.models.PointsQueue import PointsQueue
from src.models.Side import Side
from src.models.Square import Square

test_cases = [
    [
        {(1, 1), (3, 3)},
        Square(0, 4, 0, 4),
        [Square(0, 4, 0, 3), Square(1, 4, 0, 4), Square(0, 4, 1, 4), Square(0, 3, 0, 4)]
    ],
    # [{(1, 1)}, Square(0, 4, 0, 4), Square(0, 4, 0, 4)],
]


class MyTestCase(unittest.TestCase):
    @parameterized.expand(test_cases)
    def test_brute_force_resolver(self, points, square, solution):
        # given
        resolver = BruteForceSolution(square.copy(), points)

        # when
        computed_solution = resolver.compute_solution()

        # then
        self.assertCountEqual(computed_solution, solution)

    @parameterized.expand(test_cases)
    def test_border_resolver(self, points, square, solution):
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
