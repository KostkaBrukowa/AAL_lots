from typing import Set, Tuple

from src.models.PointsQueue import Point
from src.models.Side import Side
from src.models.Square import Square


class PointsSolution:
    def __init__(self, square: Square, points: Set[Tuple[int, int]]):
        self.points = points
        self.square = square

        points_to_sort = frozenset(points).union([(0, 0), (square.right_border, square.top_border)])
        self.x_sorted_arr = list(set(point[0] for point in sorted(points_to_sort, key=lambda point: point[0])))
        self.y_sorted_arr = list(set(point[1] for point in sorted(points_to_sort, key=lambda point: point[1])))
        # self.y_sorted_arr = [point[1] for point in sorted(points_to_sort, key=lambda point: point[1])]
        # self.x_sorted_arr = sorted(points_to_sort, key=lambda point: point[0])
        # self.y_sorted_arr = sorted(points_to_sort, key=lambda point: point[1])

        self.x_points_map = {point: index for index, point in enumerate(self.x_sorted_arr)}
        self.y_points_map = {point: index for index, point in enumerate(self.y_sorted_arr)}

    def compute_solution(self):
        return max((self.biggest_lot(point) for point in self.points), key=lambda square: square.area())

    def biggest_lot(self, point: Point):
        x_arr_index = self.x_points_map[point[0]]
        y_arr_index = self.y_points_map[point[1]]

        smallest_lot = Square(self.x_sorted_arr[x_arr_index - 1], self.x_sorted_arr[x_arr_index + 1],
                              self.y_sorted_arr[y_arr_index - 1], self.y_sorted_arr[y_arr_index + 1])

        for side in Side:
            i = 2
            while not self._point_on_side(side, smallest_lot):
                next_point = self._next_point(side, x_arr_index, y_arr_index, i)

                smallest_lot = smallest_lot.move_side((next_point, next_point), side)

                i += 1

        return smallest_lot

    def _point_on_side(self, side: Side, square: Square):
        if self._square_contains_edge(side, square):
            return True

        for point in self.points:
            if square.is_point_on_border(point, side):
                return True

        return False

    def _next_point(self, side: Side, x_arr_index: int, y_arr_index: int, count: int):
        if side == Side.LEFT:
            return self.x_sorted_arr[x_arr_index - count]
        if side == Side.RIGHT:
            return self.x_sorted_arr[x_arr_index + count]
        if side == Side.BOTTOM:
            return self.y_sorted_arr[y_arr_index - count]
        if side == Side.TOP:
            return self.y_sorted_arr[y_arr_index + count]

    def _square_contains_edge(self, side: Side, square: Square):
        if side == Side.LEFT:
            return square.left_border == self.square.left_border
        if side == Side.RIGHT:
            return square.right_border == self.square.right_border
        if side == Side.BOTTOM:
            return square.bottom_border == self.square.bottom_border
        if side == Side.TOP:
            return square.top_border == self.square.top_border
