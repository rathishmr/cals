import pytest
from calc import CalculatorLogic

@pytest.fixture
def calc():
    return CalculatorLogic()


@pytest.mark.security
def test_import_injection(calc):
    assert calc.evaluate("__import__('os')") == "Error"


@pytest.mark.security
def test_system_command(calc):
    assert calc.evaluate("__import__('os').system('ls')") == "Error"


@pytest.mark.security
def test_lambda_execution(calc):
    assert calc.evaluate("(lambda x: x)(5)") == "Error"


@pytest.mark.security
def test_exec_statement(calc):
    assert calc.evaluate("exec('print(5)')") == "Error"


@pytest.mark.security
def test_attribute_access(calc):
    assert calc.evaluate("(1).__class__") == "Error"
