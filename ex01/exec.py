import argparse

def convert(arg):
    return arg[::-1].swapcase()

def main(args):
    print(' '.join(map(convert, args)))

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    return args

if __name__ == "__main__":
    main(get_args()[::-1])