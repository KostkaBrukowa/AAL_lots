from command_line_config import create_parser
from src.BruteForceSolution import BruteForceSolution
from src.PointsSolution import PointsSolution
from src.Solution import Solution
from src.models.Square import Square
from src.random_generator.random_problem import generate_problem
import matplotlib.pyplot as plt
import random


def draw_square(square: Square, *, index: float = 0, color: str = None):
    plt.plot((square.left_border, square.left_border), (square.bottom_border, square.top_border), color=color)
    plt.plot((square.left_border, square.right_border), (square.top_border, square.top_border), color=color)
    plt.plot((square.right_border, square.right_border), (square.top_border, square.bottom_border), color=color)
    plt.plot((square.right_border, square.left_border), (square.bottom_border, square.bottom_border), color=color)


def draw_points(points_set):
    # plt.xlim(-1, 10)
    # plt.ylim(-1, 10)

    x = [point[0] for point in points_set]
    y = [point[1] for point in points_set]

    plt.scatter(x, y)


if __name__ == '__main__':
    random.seed(51)
    args = vars(create_parser().parse_args())
    if args['m2']:
        a, b, p = args['a'], args['b'], args['p']

        points = generate_problem(a, b, p)
        square = Square(0, a, 0, b)
        draw_points(points)
        draw_square(square, color="teal")

        # test = [{(1, 1), (3, 3)}, Square(0, 4, 0, 4), [Square(0, 4, 0, 3)]]
        # points = test[0]
        # square = test[1]
        # draw_square(square, color="teal")
        # draw_points(points)

        # resolver = Solution(square, points)
        # resolver = BruteForceSolution(square, points)
        resolver = PointsSolution(square, points)
        solutions = resolver.compute_solution()
        print(solutions)
        for index, solution in enumerate(solutions):
            print(f"Area of solution is {solution.area()}")
            draw_square(solution, index=index)

        plt.show()
