import pytest
import operator
import random
from calc import CalculatorLogic


@pytest.fixture(scope="module")
def calc():
    return CalculatorLogic()


# ---------- Operators ----------

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


# ---------- Generate Random Test Data ----------

expressions = []

for _ in range(5):

    a = random.randint(1, 10)
    b = random.randint(1, 10)

    symbol, func = random.choice(list(ops.items()))
    
    expression = f"{a}{symbol}{b}"
    expected = str(func(a, b))
    expressions.append((expression, expected))


# ---------- Tests ----------

@pytest.mark.smoke
@pytest.mark.parametrize("expression, expected", expressions)
def test_basic_operations(calc, expression, expected):
    result = calc.evaluate(expression)
    assert result == expected
