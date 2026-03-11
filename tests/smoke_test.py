import pytest
import operator
from calc import CalculatorLogic


@pytest.fixture(scope="module")
def calc():
    return CalculatorLogic()


# ---------- Dynamic Test Data ----------

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

numbers = range(1, 6)

expressions = []

for a in numbers:
    for b in numbers:
        for symbol, func in ops.items():

            expression = f"{a}{symbol}{b}"
            expected = str(func(a, b))

            expressions.append((expression, expected))


# ---------- Tests ----------

@pytest.mark.smoke
@pytest.mark.parametrize("expression, expected", expressions)
def test_basic_operations(calc, expression, expected):

    result = calc.evaluate(expression)

    assert result == expected
