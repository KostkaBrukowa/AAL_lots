import time
from typing import Set, Callable

from src.data.plots.DrawSolution import show_result
from src.data.random_generator.random_problem import generate_problem
from src.solutions.BruteForceResolver import BruteForceResolver
from src.solutions.InsideOutResolver import InsideOutResolver
from src.solutions.OutsideInResolver import OutsideInResolver
from src.solutions.models.PointsQueue import Point
from src.solutions.models.Square import Square


def compute_solution(args, square: Square, points: Set[Point]) -> [Square]:
    if args['bt']:
        return BruteForceResolver(square, points).compute_solution()
    if args['oi']:
        return OutsideInResolver(square, points).compute_solution()
    if args['io']:
        return InsideOutResolver(square, points).compute_solution()


def solve_instance(args, points_count: int, width: int, height: int) -> Callable[[], any]:
    def _solve_instance():
        square, points = generate_problem(width * 3, height * 3, points_count)
        return square, compute_solution(args, square, points), points

    return _solve_instance


def mean_time_execution(function, repeat=1):
    start = time.time()
    for _ in range(repeat):
        function()
    end = time.time()

    return (end - start) / repeat


def analyze(args, start_points_count: int, start_width: int, start_height: int, points_step_size: int,
            width_step_size: int, height_step_size: int, steps: int, step_repeat_count: int):
    for i in range(steps):
        points_count = start_points_count + i * points_step_size
        width = start_width + i * width_step_size
        height = start_height + i * height_step_size

        mean_time = mean_time_execution(solve_instance(args, points_count, width, height), step_repeat_count)

        show_result(*solve_instance(args, points_count, width, height)())

        print(f"mean_time {mean_time} step {i} points {points_count} width {width} height {height}")
