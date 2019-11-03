from typing import Tuple, Set

from src.models.PointsQueue import PointsQueue
from src.models.Side import Side
from src.models.Square import Square


def min_elements(iterable, key):
    min_element = min(iterable, key=key)
    min_value = key(min_element)

    return [element for element in iterable if key(element) == min_value]


class Solution:
    def __init__(self, square: Square, *, points: Set[Tuple[int, int]] = None, points_queue=None, solutions=[],
                 max_area=0):
        self.points = points
        self.square = square
        self.solutions = solutions
        self.max_area = max_area
        self.points_queue = points_queue if points_queue is not None else PointsQueue(self.square, points=points)

    def copy(self, square: Square):
        new_points_queue = self.points_queue.copy(square)
        new_solution = Solution(square, points=self.points, points_queue=new_points_queue, solutions=self.solutions,
                                max_area=self.max_area)

        return new_solution

    def _compute_solution(self):
        edge_points = [self.points_queue.get_edge_point(side) for side in Side]

        # if self.points_queue.empty() or self.square.area() < self.max_area:
        if self.points_queue.empty():
            return None

        if self._is_square_lot():
            # if self.square.area() > self.max_area:
            #     self.max_area = self.square.area()
            #     self.solutions = []

            return self.square

        lowest_area_loss_edge_points = min_elements(edge_points, key=lambda it: self.square.lost_area(*it))

        for side, point in lowest_area_loss_edge_points:
            resolver = self.copy(self.square.move_side(side, point))
            solution = resolver._compute_solution()

            if solution:
                self.solutions.append(solution)

    def compute_solution(self):
        self._compute_solution()

        return self.solutions

    def _is_square_lot(self):
        return len(self.points_queue.horizontal_queue) == 1
