from typing import Set

from src.models.PointsQueue import PointsQueue, Point
from src.models.Square import Square
from itertools import permutations


def generate_points_on_border(horizontal_side, vertical_side):
    border_points = []

    border_points.extend([(0, y) for y in range(vertical_side)])
    border_points.extend([(horizontal_side, y) for y in range(vertical_side)])
    border_points.extend([(x, 0) for x in range(horizontal_side)])
    border_points.extend([(x, vertical_side) for x in range(horizontal_side)])

    return set(border_points)


class BruteForceSolution:
    def __init__(self, square: Square, points: Set[Point]):
        self.square = square

        points_on_border = generate_points_on_border(square.right_border, square.top_border)
        self.points = points.union(points_on_border)

    def _is_square_lot(self, square):
        points_inside = 0

        for point in self.points:
            if square.is_point_inside(point):
                points_inside += 1

            if points_inside > 1:
                return False

        return points_inside != 0

    def compute_solution(self):
        all_squares = (Square.out_of_points(*points) for points in permutations(self.points, 4))

        lot_squares = (square for square in all_squares if self._is_square_lot(square))

        return max(lot_squares, key=lambda s: s.area())
