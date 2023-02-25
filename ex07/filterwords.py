import argparse
import sys

sys.tracebacklimit = 0
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def preprocess(str) -> str:
    for i in punctuation:
        str = str.replace(i, ' ')
    return str

def main(args : list) -> None:
    ret = [i for i in preprocess(args[0]).split() if len(i) > args[1]]    
    print(ret)

def print_error(msg : str) -> None:
    print(msg)
    exit()

def validate_args(args : list) -> None:
    if len(args) != 2: print_error("ERROR")
    try:
        args[0] = str(args[0])
        args[1] = int(args[1])
    except:
        print_error("ERROR")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    validate_args(args)
    args[1] = int(args[1])
    return args

if __name__ == "__main__":
    main(get_args())