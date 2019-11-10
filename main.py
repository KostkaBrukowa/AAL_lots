from typing import Set

from src.data.plots.DrawSolution import show_result
from src.data.random_generator.random_problem import generate_problem
from src.modes.command_line_config import create_parser
from src.modes.filemode.FileReader import read_file, save_result_to_file
from src.modes.tablemode.Analizer import analyze
from src.solutions.BruteForceSolution import BruteForceSolution
from src.solutions.PointsSolution import PointsSolution
from src.solutions.Solution import Solution
from src.solutions.models.PointsQueue import Point
from src.solutions.models.Square import Square


def compute_solution(args, square: Square, points: Set[Point]) -> [Square]:
    if args['bt']:
        return BruteForceSolution(square, points).compute_solution()
    if args['oi']:
        return Solution(square, points).compute_solution()
    if args['io']:
        return PointsSolution(square, points).compute_solution()

    raise Exception('No -bt -oi -io flag was passed')


def read_int_args(args, *flags):
    return [int(args[arg]) for arg in flags]


if __name__ == '__main__':
    args = vars(create_parser().parse_args())
    print(args)

    if args['m1']:
        filename = args['f']
        square, points = read_file(filename)
        print(square, points)
        result_squares = compute_solution(args, square, points)
        save_result_to_file(result_squares)
        show_result(square, result_squares, points)

    if args['m2']:
        points_count, width, height = read_int_args(args, 'n', 'w', 'ht')
        square, points = generate_problem(width, height, points_count)
        show_result(square, [], points)
        result_squares = compute_solution(args, square, points)
        show_result(square, result_squares, points)
        save_result_to_file(result_squares)

    if args['m3']:
        analyze(args, *read_int_args(args, 'p', 'w', 'ht', 'pstep', 'wstep', 'hstep', 'k', 'r'))
