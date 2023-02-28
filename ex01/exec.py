
# * import
# --------------------------------------------------------------------------
import sys
import argparse

# * config
# --------------------------------------------------------------------------
sys.tracebacklimit = 0


# * error_massege
# --------------------------------------------------------------------------
msg = {
    "usage" : "Usage : Python3 exec.py [string]" 
}

# * main
# --------------------------------------------------------------------------
def convert_and_swap(arg):
    return arg[::-1].swapcase()

def main(args):
    print(' '.join(map(convert, args[::-1])))

def validate_arg(args : list) -> None:
    assert len(args) >= 1 and str(args[0]), msg["usage"]
    return

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    validate_arg(args)
    return args

if __name__ == "__main__":
    main(get_args())