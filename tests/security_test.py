import pytest
from calc import CalculatorLogic


@pytest.fixture
def calc():
    return CalculatorLogic()


@pytest.mark.security
@pytest.mark.parametrize("malicious_input", [

    # 1️⃣ Import injection attempt
    "__import__('os')",

    # 2️⃣ System command execution attempt
    "__import__('os').system('dir')",

    # 3️⃣ Lambda execution attempt
    "(lambda x: x)(5)",

    # 4️⃣ Exec statement attempt
    "exec('print(5)')",

    # 5️⃣ Attribute access attempt
    "(1).__class__",

])
def test_malicious_code_blocked(calc, malicious_input):
    """
    Ensure that dangerous or malicious expressions
    are blocked and return 'Error'
    """
    assert calc.evaluate(malicious_input) == "Error"
