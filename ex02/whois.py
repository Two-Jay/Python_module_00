
# * import
# --------------------------------------------------------------------------
import argparse
import sys

# * config
# --------------------------------------------------------------------------
sys.tracebacklimit = 0

# * error_massege
# --------------------------------------------------------------------------
msg = {
    "argument" : {
        "minimum" : 'Parameter must be at least one',
        "maximum" : 'more than one argument are provided',
        "type" : 'argument is not an integer'
    }
}

# * global variables
# --------------------------------------------------------------------------
EVEN = 'Even'
ODD = 'Odd'
ZERO = 'Zero'

# * main
# --------------------------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    return args

def validate_args(args):
    assert len(args) != 0, msg['argument']['minimum']
    assert len(args) == 1, msg['argument']['maximum']
    assert args[0].isdigit(), msg['argument']['type']

def check_answer(args):
    return ZERO if int(args[0]) == 0 else EVEN if int(args[0]) % 2 == 0 else ODD

def print_answer(result : str):
    print(f'I\'m {result}.')

def main(args):
    validate_args(args)
    print_answer(check_answer(args))

if __name__ == "__main__":
    main(get_args())