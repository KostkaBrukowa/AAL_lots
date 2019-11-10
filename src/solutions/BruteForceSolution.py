from typing import Set

from itertools import permutations

from src.solutions.PointsSolution import max_elements
from src.solutions.models.PointsQueue import Point
from src.solutions.models.Square import Square


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
        self.visited_squares = set()

        points_on_border = generate_points_on_border(square.right_border, square.top_border)
        self.points = points.union(points_on_border)

    @staticmethod
    def is_square_lot(points: Set[Point], square: Square):
        points_inside = 0

        for point in points:
            if square.is_point_inside(point):
                points_inside += 1

            if points_inside > 1:
                return False

        return points_inside != 0

    def compute_solution(self):
        all_squares = (Square.out_of_points(*points) for points in permutations(self.points, 4))

        return max_elements(self._find_square_lots(all_squares), key=lambda s: s.area())
        # return max(lot_squares, key=lambda s: s.area())

    def _find_square_lots(self, all_squares):
        for square in all_squares:
            if square in self.visited_squares:
                continue

            self.visited_squares.add(square)
            if self.is_square_lot(self.points, square):
                yield square
