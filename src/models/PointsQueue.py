from collections import deque
from typing import Tuple, Set

from src.models.Side import Side
from src.models.Square import Square


class PointsQueue:
    def __init__(self, points: Set[Tuple[int, int]], square: Square):
        self.points = points
        self.square = square
        self.removed_points = set()

        points_list = list(points)

        self.horizontal_queue = deque(sorted(points_list, key=lambda point: point[0]))
        self.vertical_queue = deque(sorted(points_list, key=lambda point: point[1]))

        self.config = {
            Side.TOP: {
                'queue': self.vertical_queue,  # depending on the side horizontal or vertical queue
                'getter': lambda queue: queue[-1],  # depending on the side front or back of the queue
                'remover': lambda queue: queue.pop(),  # depending on the side front or back of the queue
                'dominant': lambda point: point[1]  # depending on the side X or Y value of point
            },
            Side.BOTTOM: {
                'queue': self.vertical_queue,
                'getter': lambda queue: queue[0],
                'remover': lambda queue: queue.popleft(),
                'dominant': lambda point: point[1]
            },
            Side.RIGHT: {
                'queue': self.horizontal_queue,
                'getter': lambda queue: queue[-1],
                'remover': lambda queue: queue.pop(),
                'dominant': lambda point: point[0]
            },
            Side.LEFT: {
                'queue': self.horizontal_queue,
                'getter': lambda queue: queue[0],
                'remover': lambda queue: queue.popleft(),
                'dominant': lambda point: point[0]
            }
        }

    def get_edge_point(self, side: Side):
        queue = self.config[side]['queue']
        get_element = self.config[side]['getter']
        remove_element = self.config[side]['remover']

        while queue:
            element = get_element(queue)

            # if element in self.points:
            #     return element, side

            if self.square.is_point_inside(element):
                return element, side

            remove_element(queue)

        return None

    # def clear_side(self, side):
    #     queue = self.config[side]['queue']
    #     get_element = self.config[side]['getter']
    #     remove_element = self.config[side]['remover']
    #     dominant = self.config[side]['dominant']
    #
    #     first_element = get_element(queue)
    #
    #     while queue:
    #         current_element, _ = self.get_edge_point(side)
    #         if dominant(current_element) != dominant(first_element):
    #             return
    #
    #         remove_element(queue)
    #         self.points.remove(current_element)
