import pytest
from calc import CalculatorLogic


@pytest.fixture
def calc():
    return CalculatorLogic()


@pytest.mark.security
@pytest.mark.parametrize("malicious_input", [

    "__import__('os')",

    "__import__('os').system('dir')",

    "(lambda x: x)(5)",

    "exec('print(5)')",

    "(1).__class__",

])
def test_malicious_code_blocked(calc, malicious_input):
    """
    Ensure that dangerous or malicious expressions
    are blocked and return 'Error'
    """
    assert calc.evaluate(malicious_input) == "Error"
