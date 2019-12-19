from typing import Set, Tuple

from src.solutions.models.Square import Square
from src.solutions.utils.types import Point


def parse_square(square_str: str) -> Square:
    width, height = square_str.split(', ')

    return Square(0, int(width), 0, int(height))


def parse_point(point_str: str) -> Point:
    x_str, y_str = point_str.split(', ')

    return int(x_str), int(y_str)


def square_to_string(square: Square) -> str:
    return f'{square.right_border}, {square.top_border}'


def read_file(filename: str) -> Tuple[Square, Set[Point]]:
    with open(filename, "r") as file:
        square = parse_square(file.readline())
        points = {parse_point(point) for point in file}

        return square, points


def save_result_to_file(squares: [Square], filename='output.txt', ):
    with open(filename, "w+") as file:
        for square in squares:
            square_str = f"{str(square)}\n"
            file.write(square_str)
            print(square_str)
