
# * import
# --------------------------------------------------------------------------
from abc import *
import argparse

# * message
# --------------------------------------------------------------------------
msg = {
    "notice" : {
        "user_input" : "What is the text to analyse?\n"
    },
    "error" : {
        "parameter" : "You must provide a string as argument",
        "type" : "argument is not a string"
    }
}

# * Class : AnalyzerStrategy <- ABCMeta
# --------------------------------------------------------------------------
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

# * Class : CountAnalyzer <- AnalyzerStrategy
# --------------------------------------------------------------------------
class CountAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "character(s)"

    def condition(self, char):
        return True

    def display(self):
        print(f"The text contains {self.count} {self.keyword}:")

# * Class : UpperAnalyzer <- AnalyzerStrategy
# --------------------------------------------------------------------------
class UpperAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "upper letter(s)"

    def condition(self, char):
        return char.isupper()

    def display(self):
        print(f"- {self.count} {self.keyword}")

# * Class : LowerAnalyzer <- AnalyzerStrategy
# --------------------------------------------------------------------------
class LowerAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "lower letter(s)"

    def condition(self, char):
        return char.islower()

    def display(self):
        print(f"- {self.count} {self.keyword}")

# * Class : PunctuationAnalyzer <- AnalyzerStrategy
# --------------------------------------------------------------------------
class PunctuationAnalyzer(AnalyzerStrategy):
    punctuation = ["!", "?", ".", ",", ";", ":", "-", "_", "'", '"']

    def __init__(self):
        self.count = 0
        self.keyword = "punctuation mark(s)"

    def condition(self, char):
        return char in self.punctuation
    
    def display(self):
        print(f"- {self.count} {self.keyword}")

# * Class : SpaceAnalyzer <- AnalyzerStrategy
# --------------------------------------------------------------------------
class SpaceAnalyzer(AnalyzerStrategy):
    def __init__(self):
        self.count = 0
        self.keyword = "space(s)"

    def condition(self, char):
        return char.isspace()

    def display(self):
        print(f"- {self.count} {self.keyword}")

# * Class : TextAnalyzer
# --------------------------------------------------------------------------
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

# * main
# --------------------------------------------------------------------------
def validate_arguments(args):
    if len(args) != 0:
        args.append(input(msg['notice']['user_input']))
    assert len(args) == 1, msg['error']['parameter']
    assert type(args[0]) == str, msg['error']['type']

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