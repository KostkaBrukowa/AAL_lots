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

    def _points_left_inside(self):
        return len(self.points) - len(self.points_queue.removed_points)

    def _is_square_lot(self):
        return self._points_left_inside() == 1

    def compute_solution(self):
        while self.points:
            edge_points = [self.points_queue.get_edge_point(side) for side in Side]

            if self._is_square_lot():
                return self.square

            point, side = min(edge_points, key=lambda edge_point: self.square.lost_area(edge_point[1], edge_point[0]))

            self.square.move_side(side, point)

        return None
