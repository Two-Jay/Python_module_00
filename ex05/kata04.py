# * kata value
# --------------------------------------------------------------------------
kata = (0, 4, 132.42222, 10000, 12345.67)

# * main
# --------------------------------------------------------------------------
def validate(kata : tuple) -> bool:
    return type(kata) == tuple and len(kata) == 5 and \
        all(type(i) == int for i in [kata[0], kata[1], kata[3]]) and all(type(i) == float for i in [kata[2], kata[4]])

def do_kata(kata : tuple) -> None:
    if validate(kata) == True:
        print(f'module_{kata[0]:0>2}, ex_{kata[1]:0>2} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}')

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()