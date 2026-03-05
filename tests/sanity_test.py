import pytest
from calc_v2 import ScientificCalculator


@pytest.fixture
def calc():
    return ScientificCalculator()


@pytest.mark.sanity
def test_square(calc):
    assert calc.square("5") == "25.0"


@pytest.mark.sanity
def test_sqrt(calc):
    assert calc.sqrt("16") == "4.0"


@pytest.mark.sanity
def test_sin(calc):
    assert round(float(calc.sin("90")), 2) == 1.00


@pytest.mark.sanity
def test_log(calc):
    assert calc.log("100") == "2.0"


@pytest.mark.sanity
def test_factorial(calc):
    assert calc.factorial("5") == "120"
