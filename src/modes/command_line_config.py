import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='Calculates biggest area inside rectangle')
    parser.add_argument('-m1', action='store_true', help='Read data from standard input and save to standard output')
    parser.add_argument('-m2', action='store_true',
                        help='Specify -a -b -p argument witch are horizontal side, vertical side number of points '
                             'respectively')
    parser.add_argument('-m3', action='store_true', help='Specify -n -k -step -r')

    parser.add_argument('-f', help='Filename to read data from', default='test_filename.txt')

    parser.add_argument('-w', help='Width of a rectangle')
    parser.add_argument('-ht', help='Height of rectangle')
    parser.add_argument('-p', help='P is number of points inside the rectangle')

    parser.add_argument('-n', help='starting n which is number of points in rectangle')
    parser.add_argument('-k', help='number of steps')
    parser.add_argument('-pstep', help='points step size')
    parser.add_argument('-wstep', help='width step size')
    parser.add_argument('-hstep', help='height step size')
    parser.add_argument('-r', help='step repeat count')

    parser.add_argument('-bt', action='store_true', help='brute force alg')
    parser.add_argument('-oi', action='store_true', help='outside in alg')
    parser.add_argument('-io', action='store_true', help='inside out alg', default=True)

    return parser
