# * kata value
# --------------------------------------------------------------------------
kata = "The right format"
kata_long = "123456789a123456789b123456789c123456789d123456789"


# * main
# --------------------------------------------------------------------------
def do_kata(kata : str) -> None:
    print(f"{kata[0:42]:->42}", end='')

def main():
    do_kata(kata)
    do_kata(kata_long)

if __name__ == "__main__":
    main()



#     For each kata, verify the exactitude of the formating with the subject

# kata00 : with tuples of different sizes, as well as an empty one

# kata01 : with dictionaries of different sizes, as well as an empty one

# kata02 : with a tuples of 5 numbers (hour, minute, year, month, day) hour, minute, month and day
# must have a minimum width of 2 and fill character set to '0' year must have a minimum width of 4 and
# fill character set to '0'

# kata03 : with strings of varying sizes (below 43 characters), as well as one empty string They must be
# printed without ending '\n', and must output exactly 42 characters.

# kata04 : with a tuples of 5 numbers.
# 1st and 2nd elements must have a minimum width of 2 and fill character set to '0'
# 3rd element must be displayed with a precision of 2
# 4th and 5th elements must be displayed with scientific notation and a precision of 2