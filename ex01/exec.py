import argparse

def convert(arg):
    ret = ''
    for i in range(len(arg)):
        if arg[i].islower():
            ret += arg[i].upper()
        elif arg[i].isupper():
            ret += arg[i].lower()
        else:
            ret += arg[i]
    return ret[::-1]

def main(args):
    print(' '.join(map(convert, args)))

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    return args

if __name__ == "__main__":
    main(get_args()[::-1])