# * kata value
# --------------------------------------------------------------------------
kata = (2019, 9, 25, 3, 30)

# * main
# --------------------------------------------------------------------------
def do_kata(kata : tuple) -> None:
    if len(kata) == 5:
        print(f"{kata[1]:0>2}/{kata[2]:0>2}/{kata[0]:0>4} {kata[3]:0>2}:{kata[4]:0>2}")

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()