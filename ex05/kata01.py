# * kata value
# --------------------------------------------------------------------------
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

# * main
# --------------------------------------------------------------------------
def do_kata(kata : dict)
    for key, value in kata.items():
        print(f"{key} was created by {value}")

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()