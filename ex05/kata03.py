# * kata value
# --------------------------------------------------------------------------
kata = "The right format"

# * main
# --------------------------------------------------------------------------
def do_kata(kata : str) -> None:
    print(f"{kata:->42}", end='')

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()