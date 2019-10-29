from src.models.PointsQueue import PointsQueue
from src.models.Square import Square


class Solution:
    def __init__(self, horizontal_side, vertical_side, points, debug=True):
        self._debug = debug
        self.square = Square((0, 0), (0, vertical_side), (horizontal_side, 0), (horizontal_side, vertical_side))
        self.points = points
        self.points_queue = PointsQueue(points)

        print(f'initialized with {horizontal_side, vertical_side, points}')

    def _is_square_lot_slow(self, square_points):
        top_x = max(square_points, key=lambda p: p[0])
        low_x = min(square_points, key=lambda p: p[0])
        top_y = max(square_points, key=lambda p: p[1])
        low_y = min(square_points, key=lambda p: p[1])

        for point in self.points:
            x, y = point
            if x < low_x or x > top_x or y < low_y or y > top_y:
                return False

        return True

    def _is_square_lot(self, square_points):
        lot = len(self.points) <= 1

        if self._debug:
            lot_debug = self._is_square_lot_slow(square_points)
            if lot != lot_debug:
                raise Exception(f'there was a mistake in lot definition {square_points}')

        return lot

    def compute_solution(self):
        return 42
