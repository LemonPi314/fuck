import argparse

from .pyfuck import Brainfuck


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    with open(args.path, 'r') as file:
        code = file.read()
    bf = Brainfuck()
    bf.run(code)
