"""
Main module
"""

from .calculator import OneModeCalculator
from .strategy import Add, Divide, Multiply, Subtract

if __name__ == "__main__":
    calculator = OneModeCalculator()
    ARG1 = 2
    ARG2 = 6.1

    for mode in [Add, Divide, Multiply, Subtract]:
        calculator.mode = mode()
        print(
            f'result when calculater is in {mode.__name__} mode is {calculator.calculate(ARG1, ARG2)}'
            )
