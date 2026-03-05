import math
from calc import CalculatorLogic


class ScientificCalculator(CalculatorLogic):

    def square(self, value: str) -> str:
        try:
            num = float(value)
            return str(num ** 2)
        except Exception:
            return "Error"

    def sqrt(self, value: str) -> str:
        try:
            num = float(value)
            if num < 0:
                return "Error"
            return str(math.sqrt(num))
        except Exception:
            return "Error"

    def sin(self, value: str) -> str:
        try:
            num = float(value)
            return str(math.sin(math.radians(num)))
        except Exception:
            return "Error"

    def log(self, value: str) -> str:
        try:
            num = float(value)
            if num <= 0:
                return "Error"
            return str(math.log10(num))
        except Exception:
            return "Error"

    def factorial(self, value: str) -> str:
        try:
            num = int(float(value))
            if num < 0:
                return "Error"
            return str(math.factorial(num))
        except Exception:
            return "Error"
