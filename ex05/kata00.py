kata = (19,42,21)

def do_kata(kata : tuple) -> None:
    print(
        f'The 3 numbers are:',
        ' '.join([f'{i}' for i in kata])
    )

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()