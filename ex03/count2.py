from abc import *
import argparse

## class definition start here
## AnalyzerStrategy -> ConcreteStrategy => TextAnalyzer

keyword = "list"

print(
f"""1. Count the {keyword} of characters in the text.
2. Count the {keyword} of upper letters in the text.
3. Count the {keyword} of lower letters in the text."""
)