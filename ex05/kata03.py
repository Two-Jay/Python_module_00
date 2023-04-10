# * kata value
# --------------------------------------------------------------------------
kata = "The right format"
kata_long = "123456789a123456789b123456789c123456789d123456789"


# * main
# --------------------------------------------------------------------------
def validate(kata : str) -> bool:
    return type(kata) == str

def do_kata(kata : str) -> None:
    if validate(kata):
        print(f"{kata[0:42]:->42}", end='')

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()