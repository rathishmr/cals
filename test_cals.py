import pytest
from calc import CalculatorLogic

@pytest.fixture
def calc():
    return CalculatorLogic()


def test_addition(calc):
    assert calc.evaluate("2+3") == "5"


def test_subtraction(calc):
    assert calc.evaluate("10-4") == "6"


def test_multiplication(calc):
    assert calc.evaluate("5*3") == "15"


def test_division(calc):
    assert calc.evaluate("20/4") == "5.0"


def test_invalid_expression(calc):
    assert calc.evaluate("2++") == "Error"


def test_square(calc):
    assert calc.square("4") == "16.0"


def test_sqrt(calc):
    assert calc.sqrt("16") == "4.0"


def test_sqrt_invalid(calc):
    assert calc.sqrt("abc") == "Error"
