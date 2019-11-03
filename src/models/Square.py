from typing import Tuple
from src.models.Side import Side


class Square:
    def __init__(self, a=None, b=None, c=None, d=None, square=None):
        if square is not None:
            self.top_border = square.top_border
            self.bottom_border = square.bottom_border
            self.right_border = square.right_border
            self.left_border = square.left_border
            return

        square_points = [a, b, c, d]
        self.top_border = max(square_points, key=lambda p: p[1])[1]
        self.bottom_border = min(square_points, key=lambda p: p[1])[1]
        self.right_border = max(square_points, key=lambda p: p[0])[0]
        self.left_border = min(square_points, key=lambda p: p[0])[0]

    def is_point_inside(self, point, side: Side):
        x, y = point

        if side.is_vertical():
            return self.bottom_border < y < self.top_border and self.left_border <= x <= self.right_border

        return self.left_border < x < self.right_border and self.bottom_border <= y <= self.top_border

    def is_point_at(self, point):
        x, y = point

        return self.left_border < x < self.right_border and self.bottom_border < y < self.top_border

    def lost_area(self, point: Tuple[int, int], side: Side):
        height = self.top_border - self.bottom_border
        width = self.right_border - self.left_border

        if side == Side.LEFT:
            return height * (point[0] - self.left_border)
        if side == Side.RIGHT:
            return height * (self.right_border - point[0])
        if side == Side.BOTTOM:
            return width * (point[1] - self.bottom_border)
        if side == Side.TOP:
            return width * (self.top_border - point[1])

    def area(self):
        return (self.right_border - self.left_border) * (self.top_border - self.bottom_border)

    def move_side(self, point: Tuple[int, int], side: Side):
        new_square = Square(square=self)
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
        return f"left {self.left_border} top {self.top_border} right {self.right_border} bottom {self.bottom_border}"
