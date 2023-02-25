kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

def main():
    for key, value in kata.items():
        print(f"{key} was created by {value}")

if __name__ == "__main__":
    main()