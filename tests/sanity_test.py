import pytest
from calc2 import ScientificCalculator


@pytest.fixture(scope="module")
def calc():
    return ScientificCalculator()



@pytest.mark.sanity
@pytest.mark.parametrize("value, expected", [
    ("5", "25.0"),
    ("3", "9.0"),
])
def test_square(calc, value, expected):
    assert calc.square(value) == expected


@pytest.mark.sanity
@pytest.mark.parametrize("value, expected", [
    ("16", "4.0"),
    ("25", "5.0"),
])
def test_sqrt(calc, value, expected):
    assert calc.sqrt(value) == expected


@pytest.mark.sanity
@pytest.mark.parametrize("angle, expected", [
    ("90", 1.0),
    ("0", 0.0),
])
def test_sin(calc, angle, expected):
    result = float(calc.sin(angle))
    assert result == pytest.approx(expected, rel=1e-2)


@pytest.mark.sanity
@pytest.mark.parametrize("value, expected", [
    ("100", "2.0"),
    ("10", "1.0"),
])
def test_log(calc, value, expected):
    assert calc.log(value) == expected


@pytest.mark.sanity
@pytest.mark.parametrize("value, expected", [
    ("5", "120"),
    ("3", "6"),
])
def test_factorial(calc, value, expected):
    assert calc.factorial(value) == expected
