from typing import Set

from src.solutions.models.PointsQueue import Point
from src.solutions.models.Square import Square


def is_square_lot(points: Set[Point], square: Square):
    points_inside = 0

    for point in points:
        if square.is_point_inside(point):
            points_inside += 1

        if points_inside > 1:
            return False

    return points_inside != 0
