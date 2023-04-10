# * kata value
# --------------------------------------------------------------------------
kata = (2019, 9, 25, 3, 30)

kata1 = (302, 9, 25, 3, 30)

# * main
# --------------------------------------------------------------------------
def validate(kata : tuple) -> bool:
    return isinstance(kata, tuple) and len(kata) == 5 and all(type(x) == int for x in kata)

def do_kata(kata : tuple) -> None:
    if validate(kata) == True:
        print(f"{kata[1]:0>2}/{kata[2]:0>2}/{kata[0]:0>4} {kata[3]:0>2}:{kata[4]:0>2}")

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()