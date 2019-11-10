from typing import Tuple, Set

from src.solutions.models.PointsQueue import PointsQueue
from src.solutions.models.Side import Side
from src.solutions.models.Square import Square
from src.solutions.utils.is_square_a_lot import is_square_lot


class BestSolution:
    def __init__(self):
        self.solutions = []
        self.max_area = 0
        self.visited_squares = set()


class OutsideInResolver:
    def __init__(self, square: Square, points: Set[Tuple[int, int]] = None, points_queue=None, best_solutions=None):
        self.points = points
        self.square = square
        self.best_solutions = best_solutions if best_solutions is not None else BestSolution()
        self.points_queue = points_queue if points_queue is not None else PointsQueue(self.square, points=points)

    def compute_solution(self):
        self._compute_solution()

        return self.best_solutions.solutions

    def _compute_solution(self):
        edge_points = [self.points_queue.get_edge_point(side) for side in Side]
        square_area = self.square.area()

        if self.points_queue.empty() or square_area < self.best_solutions.max_area or self.square in self.best_solutions.visited_squares:
            return None

        self.best_solutions.visited_squares.add(self.square)

        if is_square_lot(self.points, self.square) and square_area >= self.best_solutions.max_area:
            if square_area > self.best_solutions.max_area:
                self.best_solutions.max_area = square_area
                self.best_solutions.solutions = []

            return self.best_solutions.solutions.append(self.square)

        for point, side in edge_points:
            resolver = self._copy(self.square.move_side(point, side))
            resolver._compute_solution()

    def _copy(self, square: Square):
        new_points_queue = self.points_queue.copy(square)
        new_solution = OutsideInResolver(square, self.points, points_queue=new_points_queue,
                                         best_solutions=self.best_solutions)

        return new_solution
