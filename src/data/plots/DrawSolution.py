from typing import Set

from src.solutions.models.PointsQueue import Point
from src.solutions.models.Square import Square
import matplotlib.pyplot as plt


def draw_points(points_set: Set[Point]):
    x = [point[0] for point in points_set]
    y = [point[1] for point in points_set]

    plt.scatter(x, y)


def draw_square(square: Square, *, index: float = 0, color: str = "red"):
    plt.plot((square.left_border, square.left_border), (square.bottom_border, square.top_border), color=color)
    plt.plot((square.left_border, square.right_border), (square.top_border, square.top_border), color=color)
    plt.plot((square.right_border, square.right_border), (square.top_border, square.bottom_border), color=color)
    plt.plot((square.right_border, square.left_border), (square.bottom_border, square.bottom_border), color=color)


def show_result(main_square: Square, solutions: [Square], points: Set[Point]) -> None:
    draw_square(main_square, color="teal")

    draw_points(points)

    for index, solution in enumerate(solutions):
        draw_square(solution, index=index)

    plt.show()
