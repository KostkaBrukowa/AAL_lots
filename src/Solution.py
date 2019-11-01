from typing import Tuple, Set

from src.models.PointsQueue import PointsQueue
from src.models.Side import Side
from src.models.Square import Square


class Solution:
    def __init__(self, horizontal_side: int, vertical_side: int, points: Set[Tuple[int, int]], debug=True):
        self._debug = debug
        self.square = Square((0, 0), (0, vertical_side), (horizontal_side, 0), (horizontal_side, vertical_side))
        self.points = points
        self.points_queue = PointsQueue(points, self.square)

        print(f'initialized with {horizontal_side, vertical_side, points}')

    def _is_square_lot_slow(self):
        points_inside = 0

        for point in self.points:
            if self.square.is_point_inside(point):
                points_inside += 1

            if points_inside > 1:
                return False

        return points_inside != 0

    def _is_square_lot(self):
        lot = len(self.points) == 1

        # if self._debug:
        #     lot_debug = self._is_square_lot_slow()
        #     if lot != lot_debug:
        #         raise Exception(f'there was a mistake in lot definition {self.square}')

        return lot

    def compute_solution(self):
        while self.points:
            point, side = min([self.points_queue.get_edge_point(side) for side in Side],
                              key=lambda edge_point: self.square.lost_area(edge_point[1], edge_point[0]))

            # self.points_queue.clear_side(side)
            self.square.move_side(side, point)
            if self._is_square_lot():
                return self.square

        return None
