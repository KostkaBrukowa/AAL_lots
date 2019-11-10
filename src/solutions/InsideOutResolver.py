from collections import defaultdict
from typing import Set, Tuple, Iterable, Callable
from bisect import bisect, insort

from src.solutions.models.PointsQueue import Point
from src.solutions.models.Side import Side
from src.solutions.models.Square import Square
from src.solutions.utils.flatten import flatten
from src.solutions.utils.max_elements import max_elements


def _square_area(square_list: [Square]) -> int:
    return square_list[0].area() if square_list else 0


class InsideOutResolver:
    def __init__(self, square: Square, points: Set[Tuple[int, int]]):
        self.points = points
        self.square = square

        points_to_sort = frozenset(points).union([(0, 0), (square.right_border, square.top_border)])
        self.sorted_x_cords = sorted(
            list(set(point[0] for point in sorted(points_to_sort, key=lambda point: point[0]))))
        self.sorted_y_cords = sorted(
            list(set(point[1] for point in sorted(points_to_sort, key=lambda point: point[1]))))

        self.x_cord_to_index_map = {x_coord: index for index, x_coord in enumerate(self.sorted_x_cords)}
        self.y_cord_to_index_map = {y_coord: index for index, y_coord in enumerate(self.sorted_y_cords)}

        self.x_to_point_map = defaultdict(lambda: [0, square.top_border])
        self.y_to_point_map = defaultdict(lambda: [0, square.right_border])
        for point in points_to_sort:
            insort(self.x_to_point_map[point[0]], point[1])
            insort(self.y_to_point_map[point[1]], point[0])

    def compute_solution(self):
        return flatten(max_elements((self.biggest_lot(point) for point in self.points), key=_square_area))

    def biggest_lot(self, point: Point):
        x_cord_index = self.x_cord_to_index_map[point[0]]
        y_cord_index = self.y_cord_to_index_map[point[1]]

        smallest_lot = Square(self.sorted_x_cords[x_cord_index - 1], self.sorted_x_cords[x_cord_index + 1],
                              self.sorted_y_cords[y_cord_index - 1], self.sorted_y_cords[y_cord_index + 1])

        return max_elements(self._extend_all_sides(smallest_lot), key=lambda item: item.area())

    def _extend_all_sides(self, square: Square) -> Set[Square]:
        lots = {square}
        unmovable_sides = [side for side in Side if self._is_unmovable_side(side, square)]

        for side in Side:
            if side in unmovable_sides:
                continue

            extended_lots = self._extend_all_sides(self._extend_side(side, square))

            lots |= extended_lots

        return lots

    def _is_unmovable_side(self, side: Side, square: Square):
        return self._is_square_on_edge(side, square) or self._is_point_on_side(side, square)

    def _is_square_on_edge(self, side: Side, square: Square):
        if side == Side.LEFT:
            return square.left_border == self.square.left_border
        if side == Side.RIGHT:
            return square.right_border == self.square.right_border
        if side == Side.BOTTOM:
            return square.bottom_border == self.square.bottom_border
        if side == Side.TOP:
            return square.top_border == self.square.top_border

    def _is_point_on_side(self, side: Side, square: Square) -> bool:
        if side.is_vertical():
            points_with_same_y_cord_as_side = self.y_to_point_map[square.get_border_value(side)]
            next_larger_point_index = bisect(points_with_same_y_cord_as_side, square.left_border)

            return points_with_same_y_cord_as_side[next_larger_point_index] < square.right_border

        points_with_same_x_cord_as_side = self.x_to_point_map[square.get_border_value(side)]
        next_larger_point_index = bisect(points_with_same_x_cord_as_side, square.bottom_border)

        return points_with_same_x_cord_as_side[next_larger_point_index] < square.top_border

    def _extend_side(self, side: Side, square: Square) -> Square:
        current_square = square

        while not self._is_unmovable_side(side, current_square):
            next_point = self._get_closest_value_to_side(current_square, side)

            current_square = current_square.move_side((next_point, next_point), side)

        return current_square

    def _get_closest_value_to_side(self, square: Square, side: Side) -> int:
        current_value = square.get_border_value(side)

        if side == Side.LEFT:
            return self.sorted_x_cords[self.x_cord_to_index_map[current_value] - 1]
        if side == Side.RIGHT:
            return self.sorted_x_cords[self.x_cord_to_index_map[current_value] + 1]
        if side == Side.BOTTOM:
            return self.sorted_y_cords[self.y_cord_to_index_map[current_value] - 1]
        if side == Side.TOP:
            return self.sorted_y_cords[self.y_cord_to_index_map[current_value] + 1]
