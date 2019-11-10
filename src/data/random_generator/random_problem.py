import random

from src.solutions.models.Square import Square


def random_point(horizontal_side, vertical_side):
    return random.randint(1, horizontal_side - 1), random.randint(1, vertical_side - 1)


def generate_problem(horizontal_side, vertical_side, points_count):
    if points_count > (horizontal_side - 1) * (vertical_side - 1):
        raise Exception("Too many points")

    points = set()
    while len(points) < points_count:
        points.add(random_point(horizontal_side, vertical_side))

    return Square(0, horizontal_side, 0, vertical_side), points
