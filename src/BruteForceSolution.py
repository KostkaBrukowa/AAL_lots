from src.models.PointsQueue import PointsQueue
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
    def __init__(self, horizontal_side, vertical_side, points):
        self.square = Square.out_of_points((0, 0), (0, vertical_side), (horizontal_side, 0), (horizontal_side, vertical_side))
        self.points = points | generate_points_on_border(horizontal_side, vertical_side)

    def _is_square_lot(self, square):
        points_inside = 0

        for point in self.points:
            if square.is_point_at(point):
                points_inside += 1

            if points_inside > 1:
                return False

        return points_inside != 0

    def compute_solution(self):
        all_squares = (Square.out_of_points(*sides) for sides in permutations(self.points, 4))

        lot_squares = filter(lambda square: self._is_square_lot(square), all_squares)

        lots = list(lot_squares)
        if not len(lots):
            return 'no lot inside'

        return max(lots, key=lambda s: s.area())
