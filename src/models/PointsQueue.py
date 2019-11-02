from collections import deque
from typing import Tuple, Set

from src.models.Side import Side
from src.models.Square import Square

Point = Tuple[int, int]
QueueInfo = deque[Point] | Tuple[int, int]


class PointsQueue:
    def __init__(self,
                 points: Set[Point],
                 square: Square,
                 *,
                 horizontal_queue=None,
                 vertical_queue=None,
                 left_edge=0,
                 bottom_edge=0,
                 top_edge: int = None,
                 right_edge: int = None,
                 ):
        self.square = square
        top_edge = top_edge if top_edge is not None else len(points) - 1
        right_edge = right_edge if right_edge is not None else len(points) - 1
        self.queue_edges = {Side.LEFT: left_edge, Side.TOP: top_edge, Side.RIGHT: right_edge, Side.BOTTOM: bottom_edge}

        if horizontal_queue is not None and vertical_queue is not None:
            self.horizontal_queue, self.vertical_queue = horizontal_queue, vertical_queue
        else:
            self.horizontal_queue, self.vertical_queue = PointsQueue.generate_priority_queues(points)

        self.config = {
            Side.TOP: {
                'queue': self.vertical_queue,  # depending on the side horizontal or vertical queue
                'getter': lambda: self.vertical_queue[self.top_edge],  # front or back of the queue
                'remover': lambda: self._pop(Side.Top),  # depending on the side front or back of the queue
                'dominant': lambda point: point[1]  # depending on the side X or Y value of point
            },
            Side.BOTTOM: {
                'queue': self.vertical_queue,
                'getter': lambda: self._get_lowest_element(self.vertical_queue),
                'remover': lambda: self._pop(Side.BOTTOM),
                'dominant': lambda point: point[1]
            },
            Side.RIGHT: {
                'queue': self.horizontal_queue,
                'getter': lambda: self._get_highest_element(self.horizontal_queue),
                'remover': lambda: self._pop(Side.RIGHT),
                'dominant': lambda point: point[0]
            },
            Side.LEFT: {
                'queue': self.horizontal_queue,
                'getter': lambda: self._get_lowest_element(self.horizontal_queue),
                'remover': lambda: self._pop(Side.LEFT),
                'dominant': lambda point: point[0]
            }
        }

    @staticmethod
    def generate_priority_queues(points: Set[Point]):
        points_list = list(points)

        return (deque(sorted(points_list, key=lambda point: point[0])),
                deque(sorted(points_list, key=lambda point: point[1])))

    def _pop(self, side: Side):
        if side == Side.TOP:
            self.top_edge -= 1
        if side == Side.RIGHT:
            self.right_edge -= 1
        if side == Side.BOTTOM:
            self.bottom_edge += 1
        if side == Side.LEFT:
            self.left_edge += 1

    def _popleft(self, queue: deque[Point]):
        queue.popleft()

    def _get_lowest_element(self, queue: deque[Point]) -> Point:
        return queue[0]

    def _get_highest_element(self, queue: deque[Point]) -> Point:
        return queue[-1]

    def _get_element(self, side: Side):
        return self.config

    def get_edge_point(self, side: Side):
        queue = self.config[side]['queue']
        get_element = self.config[side]['getter']
        remove_element = self.config[side]['remover']

        while queue:
            element = get_element(queue)

            if self.square.is_point_inside(element):
                return element, side

            remove_element()

        return None
