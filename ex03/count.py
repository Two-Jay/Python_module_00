from abc import *
import argparse

## class definition start here
## AnalyzerStrategy -> ConcreteStrategy => TextAnalyzer

class AnalyzerStrategy(metaclass=ABCMeta):
    __count = 0
    __keyword = ""

    def analyze(self, char):
        if self.condition(char):
            self.count += 1

    @abstractmethod
    def condition(self, char):
        pass

    @abstractmethod
    def display(self):
        pass

class CountAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "character(s)"

    def condition(self, char):
        return True

    def display(self):
        print(f"The text contains {self.count} {self.keyword}:")

class UpperAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "upper letter(s)"

    def condition(self, char):
        return char.isupper()

    def display(self):
        print(f"- {self.count} {self.keyword}")

class LowerAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "lower letter(s)"

    def condition(self, char):
        return char.islower()

    def display(self):
        print(f"- {self.count} {self.keyword}")

class PunctuationAnalyzer(AnalyzerStrategy):
    punctuation = ["!", "?", ".", ",", ";", ":", "-", "_", "'", '"']

    def __init__(self):
        self.count = 0
        self.keyword = "punctuation mark(s)"

    def condition(self, char):
        return char in self.punctuation
    
    def display(self):
        print(f"- {self.count} {self.keyword}")

class SpaceAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "space(s)"

    def condition(self, char):
        return char.isspace()

    def display(self):
        print(f"- {self.count} {self.keyword}")

class TextAnalyzer():
    def __init__(self):
        self.analyzers = [
            CountAnalyzer(),
            UpperAnalyzer(),
            LowerAnalyzer(),
            PunctuationAnalyzer(),
            SpaceAnalyzer()
        ]

    def analyze(self, text):
        for char in text:
            for analyzer in self.analyzers:
                analyzer.analyze(char)

    def display(self):
        for analyzer in self.analyzers:
            analyzer.display()

def validate_arguments(args):
    if len(args) == 0:
        args.append(input("What is the text to analyse?\n"))
    assert len(args) == 1, "You must provide a string as argument"
    assert type(args[0]) == str, "argument is not a string"

def text_analyzer(args):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    validate_arguments(args)
    analyzer = TextAnalyzer()
    analyzer.analyze(args[0])
    analyzer.display()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    return args

def main(args):
    text_analyzer(args)

if __name__ == "__main__":
    main(get_args())