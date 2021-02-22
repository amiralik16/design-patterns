"""
Module defining the I_Operate strategies
"""

from abc import ABC, abstractmethod


class IOperate(ABC):
    """
    Strategy interface
    """

    @abstractmethod
    def execute(self, arg1: float, arg2: float) -> float:
        """
        Execution logic of the operator to be implemented by classes
        """


class Add(IOperate):
    """
    Addition Strategy
    """

    def execute(self, arg1: float, arg2: float) -> float:
        """Adds arg1 and arg2 and returns the result

        Args:
            arg1 (float): first float
            arg2 (float): second float

        Returns:
            float: addition result
        """
        return arg1 + arg2


class Subtract(IOperate):
    """
    Subtraction Strategy
    """

    def execute(self, arg1: float, arg2: float) -> float:
        """Subtracts arg2 from arg1 and returns the result

        Args:
            arg1 (float): first float
            arg2 (float): second float

        Returns:
            float: subtraction result
        """
        return arg1 - arg2


class Multiply(IOperate):
    """
    Multiplication Strategy
    """

    def execute(self, arg1: float, arg2: float) -> float:
        """Multiplies arg2 and arg1 and returns the result

        Args:
            arg1 (float): first float
            arg2 (float): second float

        Returns:
            float: multiplication result
        """
        return arg1 * arg2


class Divide(IOperate):
    """
    Division Strategy
    """

    def execute(self, arg1: float, arg2: float) -> float:
        """Divides arg2 from arg1 and returns the result

        Args:
            arg1 (float): first float
            arg2 (float): second float

        Returns:
            float: division result
        """
        return arg1 / arg2
