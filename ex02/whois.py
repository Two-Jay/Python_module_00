import argparse
import sys

sys.tracebacklimit = 0

errmsg_argument_maximum = 'more than one argument are provided'
errmsg_argument_type = 'argument is not an integer'

EVEN = 'Even'
ODD = 'Odd'
ZERO = 'Zero'

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    return args

def validate_args(args):
    assert len(args) <= 1, errmsg_argument_maximum
    assert args[0].isdigit(), errmsg_argument_type if len(args) == 1 else None

def check_answer(args):
    return ZERO if int(args[0]) == 0 else EVEN if int(args[0]) % 2 == 0 else ODD

def print_answer(result : str):
    print(f'I\'m {result}.')

def main(args):
    validate_args(args)
    print_answer(check_answer(args))

if __name__ == "__main__":
    main(get_args())