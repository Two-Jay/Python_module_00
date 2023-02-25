import argparse
import sys

sys.tracebacklimit = 0
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

morse_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

def convert_str_to_morse(str:str) -> str:
    ret = ""
    for i in range(len(str)):
        if i < len(str) - 1:
            ret += morse_dict[str[i].lower()] + " "
        else:
            ret += morse_dict[str[i].lower()]
    return ret

def main(args : list) -> None:
    if len(args) == 0:
        exit()
    ret = ""
    for i in args:
        ret += convert_str_to_morse(i)
        if i != args[-1]:
            ret += " / "
    print(ret)

def print_error(msg : str) -> None:
    print(msg)
    exit()

def validate_args(args : list) -> None:
    try:
        for i in punctuation:
            for j in args:
                if i in j: raise Exception
    except:
        print_error("ERROR")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    validate_args(args)
    return args

if __name__ == "__main__":
    main(get_args())