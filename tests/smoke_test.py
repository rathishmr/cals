import pytest
from calc import CalculatorLogic

@pytest.fixture
def calc():
    return CalculatorLogic()


@pytest.mark.smoke
def test_addition(calc):
    assert calc.evaluate("2+3") == "5"


@pytest.mark.smoke
def test_subtraction(calc):
    assert calc.evaluate("10-4") == "6"


@pytest.mark.smoke
def test_multiplication(calc):
    assert calc.evaluate("6*7") == "42"


@pytest.mark.smoke
def test_division(calc):
    assert calc.evaluate("20/5") == "4.0"


@pytest.mark.smoke
def test_parentheses(calc):
    assert calc.evaluate("(2+3)*4") == "20"
