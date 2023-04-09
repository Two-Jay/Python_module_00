kata = (19,42,21)

def validate(kata : tuple) -> bool:
    return isinstance(kata, tuple) and len(kata) == 3 and all(type(x) == int for x in kata)

def do_kata(kata : tuple) -> None:
    if validate(kata):
        print(f"The 3 numbers are:{' '.join([f'{i}' for i in kata])}")

def main():
    do_kata(kata)
    do_kata(kata2)

if __name__ == "__main__":
    main()