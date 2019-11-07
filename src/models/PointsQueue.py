from typing import Tuple, Set, List

from src.models.FixedDeque import FixedDeque
from src.models.Side import Side
from src.models.Square import Square

Point = Tuple[int, int]


class PointsQueue:
    def __init__(self, square: Square, *, horizontal_queue: FixedDeque = None, vertical_queue: FixedDeque = None,
                 points: Set[Point] = None):
        self.square = square

        if horizontal_queue is not None and vertical_queue is not None:
            self.horizontal_queue, self.vertical_queue = horizontal_queue, vertical_queue
        else:
            self.horizontal_queue, self.vertical_queue = PointsQueue.generate_queues(points)

    @staticmethod
    def generate_queues(points: Set[Point]) -> Tuple[FixedDeque, FixedDeque]:
        points_list = list(points)

        return (FixedDeque(sorted(points_list, key=lambda point: point[0])),
                FixedDeque(sorted(points_list, key=lambda point: point[1])))

    def get_edge_point(self, side: Side) -> Tuple[Point, Side]:
        while self.horizontal_queue and self.vertical_queue:
            point = self._get_element(side)

            if self._is_point_inside_square(point, side):
                return point, side

            self._pop(side)

        return None

    def empty(self):
        return len(self.horizontal_queue) == 0 or len(self.vertical_queue) == 0

    def copy(self, square: Square):
        new_horizontal_queue = self.horizontal_queue.copy()
        new_vertical_queue = self.vertical_queue.copy()

        return PointsQueue(square, horizontal_queue=new_horizontal_queue, vertical_queue=new_vertical_queue)

    def _pop(self, side: Side) -> None:
        if side == Side.TOP:
            self.vertical_queue.pop()
        if side == Side.RIGHT:
            self.horizontal_queue.pop()
        if side == Side.BOTTOM:
            self.vertical_queue.popleft()
        if side == Side.LEFT:
            self.horizontal_queue.popleft()

    def _get_element(self, side: Side) -> Point:
        if side == Side.TOP:
            return self.vertical_queue.end()
        if side == Side.RIGHT:
            return self.horizontal_queue.end()
        if side == Side.BOTTOM:
            return self.vertical_queue.front()
        if side == Side.LEFT:
            return self.horizontal_queue.front()

    def _is_point_inside_square(self, point, side: Side):
        x, y = point

        if side.is_vertical():
            return self.square.bottom_border < y < self.square.top_border and self.square.left_border <= x <= self.square.right_border

        return self.square.left_border < x < self.square.right_border and self.square.bottom_border <= y <= self.square.top_border
