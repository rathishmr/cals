import pytest
from calculator import CalculatorLogic

@pytest.fixture
def calc():
    return CalculatorLogic()


@pytest.mark.slow
def test_large_multiplication(calc):
    assert calc.evaluate("999999*999999") == str(999999*999999)


@pytest.mark.slow
def test_long_expression(calc):
    assert calc.evaluate("1+2+3+4+5+6+7+8+9+10") == "55"


@pytest.mark.slow
def test_large_square(calc):
    assert calc.square("100000") == "10000000000.0"


@pytest.mark.slow
def test_large_sqrt(calc):
    assert calc.sqrt("100000000") == "10000.0"


@pytest.mark.slow
def test_complex_expression(calc):
    assert calc.evaluate("((1000/5)*3)+200-50") == str(((1000/5)*3)+200-50)
