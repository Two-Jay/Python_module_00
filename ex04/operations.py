
# * import
# --------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod
import argparse
import sys
import decimal


# * config
# --------------------------------------------------------------------------
sys.tracebacklimit = 0


# * global variables
# --------------------------------------------------------------------------
ljust_width = 15
ljust_diverr_width = 6


# * messege
# --------------------------------------------------------------------------
msg = {
    'argument_maximum' : 'too many arguments',
    'argument_type' : 'only integers',
    'usage' : """Usage: python operations.py <number1> <number2>\nExample:\n    python operations.py 10 3""",
    'module_by_zero' : "ERROR (modulo by zero)",
    'divide_by_zero' : "ERROR (division by zero)",
}


# * Class Value
# --------------------------------------------------------------------------
class Value():
    def __init__(self, value : int):
        self.value = decimal.Decimal(value)

    def get(self):
        return self.value

# * AbstractClass Operator
# --------------------------------------------------------------------------
class Operator(metaclass=ABCMeta):
    __keyword = ''
    __result = 0

    @abstractmethod
    def operate(self, other):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

# * Class AddOperator extends Operator
# --------------------------------------------------------------------------
class AddOperator(Operator):
    __keyword = "Sum"
    __result = 0

    def operate(self, value1 : Value, value2 : Value):
        self.__result = value1.get() + value2.get()

    def __str__(self):
        return f"{self.__keyword.ljust(ljust_width)}: {self.__result}"

# * Class SubtractOperator extends Operator
# --------------------------------------------------------------------------
class SubtractOperator(Operator):
    __keyword = "Difference"
    __result = 0

    def operate(self, value1 : Value, value2 : Value):
        self.__result = value1.get() - value2.get()

    def __str__(self):
        return f"{self.__keyword.ljust(ljust_width)}: {self.__result}"

# * Class MultiplyOperator extends Operator
# --------------------------------------------------------------------------
class MultiplyOperator(Operator):
    __keyword = "Product"
    __result = 0

    def operate(self, value1 : Value, value2 : Value):
        self.__result = value1.get() * value2.get()

    def __str__(self):
        return f"{self.__keyword.ljust(ljust_width)}: {self.__result}"

# * Class DivideOperator extends Operator
# --------------------------------------------------------------------------
class DivideOperator(Operator):
    __keyword = "Quotient"
    __result = 0

    def operate(self, value1 : Value, value2 : Value):
        self.__result = value1.get() / value2.get() if value2.get() != 0 else errmsg['divide_by_zero']

    def __str__(self):
        return f"{self.__keyword.ljust(ljust_width)}: {self.__result}"

# * Class RemainderOperator extends Operator
# --------------------------------------------------------------------------
class RemainderOperator(Operator):
    __keyword = "Remainder"
    __result = 0

    def operate(self, value1 : Value, value2 : Value):
        self.__result = value1.get() % value2.get() if value2.get() != 0 else errmsg['module_by_zero']

    def __str__(self):
        return f"{self.__keyword.ljust(ljust_width)}: {self.__result}"

# * Class Calculator
# --------------------------------------------------------------------------
class Calculator():
    OperatorList = [AddOperator(), SubtractOperator(), MultiplyOperator(), DivideOperator(), RemainderOperator()]

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def operate(self):
        for operator in self.OperatorList:
            operator.operate(self.value1, self.value2)
            print(operator)

# * main
# --------------------------------------------------------------------------
def main(args):
    Calculator(Value(int(args[0])), Value(int(args[1]))).operate()

def validate_args(args):
    if len(args) <= 1:
        exit(msg['usage'])
    assert len(args) == 2, msg['argument_maximum']
    assert args[0].isdigit(), msg['argument_type']
    assert args[1].isdigit(), msg['argument_type']

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(nargs = '*', dest = 'arg')
    args = parser.parse_args().arg
    validate_args(args)
    return args

if __name__ == "__main__":
    main(get_args())