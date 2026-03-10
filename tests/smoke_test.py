import pytest
from calc import CalculatorLogic


@pytest.fixture(scope="module")
def calc():
    return CalculatorLogic()

# Basic Arithmetic Operations

@pytest.mark.smoke
@pytest.mark.parametrize("expression, expected", [
    ("2+3", "5"),
    ("10-4", "6"),
    ("6*7", "42"),
    ("20/5", "4.0"),
    ("(2+3)*4", "20"),
])
def test_basic_operations(calc, expression, expected):
    assert calc.evaluate(expression) == expected
