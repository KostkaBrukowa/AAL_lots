import random


def random_point(horizontal_side, vertical_side):
    return random.randint(1, horizontal_side), random.randint(1, vertical_side)


def generate_problem(horizontal_side, vertical_side, points_count):
    points = set()
    while len(points) < points_count:
        points.add(random_point(horizontal_side, vertical_side))

    return points
