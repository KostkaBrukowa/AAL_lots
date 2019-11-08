from collections import Counter, defaultdict
from typing import Set, Tuple, List, Iterable, Callable

from src.models.PointsQueue import Point
from src.models.Side import Side
from src.models.Square import Square


# def _get_sides_with_points_on_both_corners(corners_with_points: List[Tuple[Side, Side]]) -> [Side]:
#     sides_count = Counter(list(sum(corners_with_points, ()))).most_common(4)  # flat array of corners, each side being counted
#
# return [side for side, count in sides_count if count >= 2]

def max_elements(iterable: Iterable[any], key: Callable[[any], any]):
    max_value = None
    max_elems = []
    for item in iterable:
        item_value = key(item)
        if max_value is None or item_value > max_value:
            max_value = item_value
            max_elems = [item]

        elif item_value >= max_value:
            max_elems.append(item)

    return max_elems


def flatten(iterable: Iterable[any]):
    return [item for sublist in iterable for item in sublist]


def _square_area(square_list: [Square]) -> int:
    return square_list[0].area() if square_list else 0


class PointsSolution:
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

        # self.x_to_point_map = defaultdict(set)
        # self.y_to_point_map = defaultdict(set)
        # for point in points_to_sort:
        #     self.x_to_point_map[point[0]].add(point)
        #     self.y_to_point_map[point[1]].add(point)

    def compute_solution(self):
        return flatten(max_elements((self.biggest_lot(point) for point in self.points), key=_square_area))

    def biggest_lot(self, point: Point):
        x_cord_index = self.x_cord_to_index_map[point[0]]
        y_cord_index = self.y_cord_to_index_map[point[1]]

        smallest_lot = Square(self.sorted_x_cords[x_cord_index - 1], self.sorted_x_cords[x_cord_index + 1],
                              self.sorted_y_cords[y_cord_index - 1], self.sorted_y_cords[y_cord_index + 1])

        unmovable_sides = [side for side in Side if self._is_unmovable_side(side, smallest_lot)]

        return max_elements(self._extend_all_sides(unmovable_sides, smallest_lot), key=lambda item: item.area())

    def _extend_all_sides(self, unmovable_sides: List[Side], square: Square) -> Set[Square]:
        lots = {square}

        for side in Side:
            if side in unmovable_sides:
                continue

            extended_lots = self._extend_all_sides([*unmovable_sides, side], self._extend_side(side, square))

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

    def _is_point_on_side(self, side: Side, square: Square):
        # TODO make this faster
        for point in self.points:
            if square.is_point_on_border(point, side):
                return True

        return False

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
