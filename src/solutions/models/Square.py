from typing import Tuple
from src.solutions.models.Side import Side


class Square:
    def __init__(self, left_border, right_border, bottom_border, top_border):
        self.top_border = top_border
        self.bottom_border = bottom_border
        self.right_border = right_border
        self.left_border = left_border

    @staticmethod
    def out_of_points(a, b, c, d):
        square_points = [a, b, c, d]

        left_border = min(square_points, key=lambda p: p[0])[0]
        right_border = max(square_points, key=lambda p: p[0])[0]
        bottom_border = min(square_points, key=lambda p: p[1])[1]
        top_border = max(square_points, key=lambda p: p[1])[1]

        return Square(left_border, right_border, bottom_border, top_border)

    def copy(self):
        return Square(self.left_border, self.right_border, self.bottom_border, self.top_border)

    def is_point_inside(self, point):
        x, y = point

        return self.left_border < x < self.right_border and self.bottom_border < y < self.top_border

    # TODO delete
    def is_point_on_border(self, point, side):
        x, y = point

        if side == Side.LEFT:
            return point[0] == self.left_border and self.bottom_border < y < self.top_border
        if side == Side.RIGHT:
            return point[0] == self.right_border and self.bottom_border < y < self.top_border
        if side == Side.BOTTOM:
            return point[1] == self.bottom_border and self.left_border < x < self.right_border
        if side == Side.TOP:
            return point[1] == self.top_border and self.left_border < x < self.right_border

    def get_border_value(self, side: Side):
        if side == Side.LEFT:
            return self.left_border
        if side == Side.RIGHT:
            return self.right_border
        if side == Side.BOTTOM:
            return self.bottom_border
        if side == Side.TOP:
            return self.top_border

    def area(self):
        return (self.right_border - self.left_border) * (self.top_border - self.bottom_border)

    def move_side(self, point: Tuple[int, int], side: Side):
        """Returns new square with side moved"""
        new_square = Square(self.left_border, self.right_border, self.bottom_border, self.top_border)
        new_square._move_side(side, point)

        return new_square

    def _move_side(self, side, point):
        if side == Side.LEFT:
            self.left_border = point[0]
        if side == Side.RIGHT:
            self.right_border = point[0]
        if side == Side.TOP:
            self.top_border = point[1]
        if side == Side.BOTTOM:
            self.bottom_border = point[1]

    def __str__(self):
        return f"left {self.left_border} right {self.right_border} bottom {self.bottom_border} top {self.top_border} area {self.area()}"

    def __repr__(self):
        return f"left {self.left_border} right {self.right_border} bottom {self.bottom_border} top {self.top_border} area {self.area()}"

    def __hash__(self):
        return hash(f"{self.left_border}-{self.top_border}-{self.right_border}-{self.bottom_border}")

    def __eq__(self, other):
        return (self.left_border == other.left_border
                and self.right_border == other.right_border
                and self.top_border == other.top_border
                and self.bottom_border == other.bottom_border
                )
