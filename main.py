from command_line_config import create_parser
from src.BruteForceSolution import BruteForceSolution
from src.Solution import Solution
from src.models.Square import Square
from src.random_generator.random_problem import generate_problem
import matplotlib.pyplot as plt
import random


def draw_square(square: Square, color: str):
    plt.plot((square.left_border, square.left_border), (square.bottom_border, square.top_border), color=color)
    plt.plot((square.left_border, square.right_border), (square.top_border, square.top_border), color=color)
    plt.plot((square.right_border, square.right_border), (square.top_border, square.bottom_border), color=color)
    plt.plot((square.right_border, square.left_border), (square.bottom_border, square.bottom_border), color=color)


def draw_points(points_set):
    plt.xlim(-10, 10)
    plt.ylim(-1, 10)

    x = [point[0] for point in points_set]
    y = [point[1] for point in points_set]

    plt.scatter(x, y)


if __name__ == '__main__':
    random.seed(50)
    args = vars(create_parser().parse_args())
    if args['m2']:
        a, b, p = args['a'], args['b'], args['p']

        points = generate_problem(a, b, p)

        draw_points(points)

        resolver = Solution(a, b, points)
        draw_square(resolver.square, "teal")

        solution = resolver.compute_solution()
        if solution:
            print(f"Area of solution is {solution.area()}")

        if solution:
            draw_square(solution, "red")

        plt.show()
