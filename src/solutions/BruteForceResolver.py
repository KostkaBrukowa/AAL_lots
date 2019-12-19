from typing import Set

from itertools import permutations

from src.solutions.models.Square import Square
from src.solutions.utils.is_square_a_lot import is_square_lot
from src.solutions.utils.max_elements import max_elements
from src.solutions.utils.types import Point


def generate_points_on_border(horizontal_side, vertical_side):
    border_points = []

    border_points.extend([(0, y) for y in range(vertical_side)])
    border_points.extend([(horizontal_side, y) for y in range(vertical_side)])
    border_points.extend([(x, 0) for x in range(horizontal_side)])
    border_points.extend([(x, vertical_side) for x in range(horizontal_side)])

    return set(border_points)


class BruteForceResolver:
    def __init__(self, square: Square, points: Set[Point]):
        self.square = square
        self.visited_squares = set()

        points_on_border = generate_points_on_border(square.right_border, square.top_border)
        self.points = points.union(points_on_border)

    def compute_solution(self):
        all_squares = (Square.out_of_points(*points) for points in permutations(self.points, 4))

        return max_elements(self._find_square_lots(all_squares), key=lambda s: s.area())

    def _find_square_lots(self, all_squares):
        for square in all_squares:
            if square in self.visited_squares:
                continue

            self.visited_squares.add(square)
            if is_square_lot(self.points, square):
                yield square
