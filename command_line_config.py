import argparse
import random


def create_parser():
    parser = argparse.ArgumentParser(description='Calculates biggest area inside rectangle')
    parser.add_argument('-m1', action='store_true', help='Read data from standard input and save to standard output')
    parser.add_argument('-m2', action='store_true',
                        help='Specify -a -b -p argument witch are horizontal side, vertical side number of points '
                             'respectively', default=True)
    parser.add_argument('-m3', action='store_true', help='Specify -start -steps -step -repeat')

    parser.add_argument('-a', help='A is the length of horizontal side', default=7)
    # parser.add_argument('-a', help='A is the length of horizontal side', default=random.randint(5, 7))
    parser.add_argument('-b', help='B is the length of vertical side', default=7)
    # parser.add_argument('-b', help='B is the length of vertical side', default=random.randint(5, 6))
    parser.add_argument('-p', help='P is number of points inside the rectangle', default=random.randint(5, 10))

    return parser
