import pytest
from calc import CalculatorLogic


@pytest.fixture(scope="module")
def calc():
    return CalculatorLogic()

# Large Expression Evaluations

@pytest.mark.slow
@pytest.mark.parametrize("expression, expected", [
    ("999999*999999", str(999999 * 999999)),
    ("1+2+3+4+5+6+7+8+9+10", "55"),
    ("((1000/5)*3)+200-50", str(((1000/5)*3)+200-50)),
])
def test_large_expressions(calc, expression, expected):
    assert calc.evaluate(expression) == expected


# Large Square

@pytest.mark.slow
def test_large_square(calc):
    result = float(calc.square("100000"))
    assert result == pytest.approx(10000000000.0)


# Large Square Root

@pytest.mark.slow
def test_large_sqrt(calc):
    result = float(calc.sqrt("100000000"))
    assert result == pytest.approx(10000.0)
