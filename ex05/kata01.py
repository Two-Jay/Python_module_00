# * kata value
# --------------------------------------------------------------------------
kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

# * main
# --------------------------------------------------------------------------
def validate(kata : dict) -> bool:
    return isinstance(kata, dict) and all(type(x) == str for x in kata.values()) and all(type(x) == str for x in kata.keys())

def do_kata(kata : dict):
    if validate(kata) == True:
        for key, value in kata.items():
            print(f"{key} was created by {value}")

def main():
    do_kata(kata)

if __name__ == "__main__":
    main()