from typing import Tuple, Set

from src.models.PointsQueue import PointsQueue
from src.models.Side import Side
from src.models.Square import Square


def min_elements(iterable, key):
    min_element = min(iterable, key=key)
    min_value = key(min_element)

    return [element for element in iterable if key(element) == min_value]


class BestSolution:
    def __init__(self):
        self.solutions = []
        self.max_area = 0
        self.visited_squares = set()


class Solution:
    def __init__(self, square: Square, *, points: Set[Tuple[int, int]] = None, points_queue=None, best_solutions=None):
        self.points = points
        self.square = square
        self.best_solutions = best_solutions if best_solutions is not None else BestSolution()
        self.points_queue = points_queue if points_queue is not None else PointsQueue(self.square, points=points)

    def copy(self, square: Square):
        new_points_queue = self.points_queue.copy(square)
        new_solution = Solution(square, points=self.points, points_queue=new_points_queue,
                                best_solutions=self.best_solutions)

        return new_solution

    def _compute_solution(self):
        edge_points = [self.points_queue.get_edge_point(side) for side in Side]
        square_area = self.square.area()

        if self.points_queue.empty() or square_area < self.best_solutions.max_area or self.square in self.best_solutions.visited_squares:
            return None

        self.best_solutions.visited_squares.add(self.square)

        if self._is_square_lot() and square_area >= self.best_solutions.max_area:
            if square_area > self.best_solutions.max_area:
                self.best_solutions.max_area = square_area
                self.best_solutions.solutions = []

            return self.square

        for point, side in edge_points:
            resolver = self.copy(self.square.move_side(point, side))
            solution = resolver._compute_solution()

            if solution:
                self.best_solutions.solutions.append(solution)

    def compute_solution(self):
        self._compute_solution()

        return self.best_solutions.solutions

    def _is_square_lot(self):
        count = 0
        for point in self.points:
            if self.square.is_point_at(point):
                count += 1

        return count == 1
