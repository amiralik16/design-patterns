"""
Module defining the calculator class
"""

from .strategy import IOperate, Add


class OneModeCalculator():
    """
    Calculator class implementation
    """

    def __init__(self, mode: IOperate = Add()):
        """This is a calculator that can only do one sort of operation at a time.
        You would have to manually change it's operation type if you want it to behave
        some other way

        Args:
            mode (I_Operate, optional): The initial operator mode of the calculator.
            Defaults to Add.
        """

        self._mode = mode

    @property
    def mode(self) -> IOperate:
        """Turns mode into a property

        Returns:
            I_Operate: mode
        """
        return self._mode

    @mode.setter
    def mode(self, mode: IOperate):
        self._mode = mode

    def calculate(self, arg1: float, arg2: float) -> float:
        """Calculates the result

        Args:
            arg1 (float): first argument
            arg2 (float): second argument

        Returns:
            float: result
        """
        return self._mode.execute(arg1, arg2)
