from command_line_config import create_parser
from src.Solution import Solution
from src.random_generator.random_problem import generate_problem

if __name__ == '__main__':
    args = vars(create_parser().parse_args())
    if args['m2']:
        a, b, p = args['a'], args['b'], args['p']

        if p > (a - 1) * (b - 1):
            print('Too many points')

        points = generate_problem(a, b, p)

        resolver = Solution(a, b, points)

        resolver.compute_solution()
