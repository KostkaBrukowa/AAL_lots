from collections import Counter, defaultdict
from typing import Set, Tuple, List

from src.models.PointsQueue import Point
from src.models.Side import Side
from src.models.Square import Square


# def _get_sides_with_points_on_both_corners(corners_with_points: List[Tuple[Side, Side]]) -> [Side]:
#     sides_count = Counter(list(sum(corners_with_points, ()))).most_common(4)  # flat array of corners, each side being counted
#
# return [side for side, count in sides_count if count >= 2]


class PointsSolution:
    def __init__(self, square: Square, points: Set[Tuple[int, int]]):
        self.points = points
        self.square = square

        points_to_sort = frozenset(points).union([(0, 0), (square.right_border, square.top_border)])
        self.x_sorted_arr = sorted(list(set(point[0] for point in sorted(points_to_sort, key=lambda point: point[0]))))
        self.y_sorted_arr = sorted(list(set(point[1] for point in sorted(points_to_sort, key=lambda point: point[1]))))

        self.x_cord_map = {point: index for index, point in enumerate(self.x_sorted_arr)}
        self.y_cord_map = {point: index for index, point in enumerate(self.y_sorted_arr)}

        # self.x_to_point_map = defaultdict(set)
        # self.y_to_point_map = defaultdict(set)
        # for point in points_to_sort:
        #     self.x_to_point_map[point[0]].add(point)
        #     self.y_to_point_map[point[1]].add(point)

    def compute_solution(self):
        return max((self.biggest_lot(point) for point in self.points), key=lambda square: square.area())

    def biggest_lot(self, point: Point):
        x_arr_index = self.x_cord_map[point[0]]
        y_arr_index = self.y_cord_map[point[1]]

        smallest_lot = Square(self.x_sorted_arr[x_arr_index - 1], self.x_sorted_arr[x_arr_index + 1],
                              self.y_sorted_arr[y_arr_index - 1], self.y_sorted_arr[y_arr_index + 1])

        unmovable_sides = [side for side in Side if self._is_unmovable_side(side, smallest_lot)]

        return self._extend_all_sides(unmovable_sides, smallest_lot)

    def _extend_all_sides(self, unmovable_sides: List[Side], square: Square) -> Square:
        max_lot = square

        for side in Side:
            if side in unmovable_sides:
                continue

            lot = self._extend_all_sides([*unmovable_sides, side], self._extend_side(side, square))

            if lot.area() > max_lot.area():
                max_lot = lot

        return max_lot

    def _square_contains_edge(self, side: Side, square: Square):
        if side == Side.LEFT:
            return square.left_border == self.square.left_border
        if side == Side.RIGHT:
            return square.right_border == self.square.right_border
        if side == Side.BOTTOM:
            return square.bottom_border == self.square.bottom_border
        if side == Side.TOP:
            return square.top_border == self.square.top_border

    def _is_point_on_side(self, side: Side, square: Square):
        # TODO make this faster
        for point in self.points:
            if square.is_point_on_border(point, side):
                return True

        return False

    def _is_unmovable_side(self, side: Side, square: Square):
        return self._square_contains_edge(side, square) or self._is_point_on_side(side, square)

    def _get_nearest_point(self, side: Side, edge_value: int) -> Point:
        current_cord_map = self.y_cord_map if side.is_vertical() else self.x_cord_map
        if side == Side.LEFT:
            return self.x_sorted_arr[current_cord_map[edge_value] - 1], 0
        if side == Side.RIGHT:
            return self.x_sorted_arr[current_cord_map[edge_value] + 1], 0
        if side == Side.BOTTOM:
            return 0, self.y_sorted_arr[current_cord_map[edge_value] - 1]
        if side == Side.TOP:
            return 0, self.y_sorted_arr[current_cord_map[edge_value] + 1]

    def _extend_side(self, side: Side, square: Square) -> Square:
        current_square = square

        while not self._is_unmovable_side(side, current_square):
            next_point = self._get_nearest_point(side, current_square.get_border_value(side))

            current_square = current_square.move_side(next_point, side)

        return current_square
