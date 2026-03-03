import pytest
from calc import CalculatorLogic


@pytest.fixture
def calc():
    return CalculatorLogic()


# =====================================================
# 1–10: Complex Operator Precedence
# =====================================================

def test_complex_precedence_1(calc):
    assert calc.evaluate("2+3*4-5") == "9"

def test_complex_precedence_2(calc):
    assert calc.evaluate("10-2*3+4") == "8"

def test_complex_precedence_3(calc):
    assert calc.evaluate("100/5*2") == "40.0"

def test_complex_precedence_4(calc):
    assert calc.evaluate("5+6/3*2") == "9.0"

def test_complex_precedence_5(calc):
    assert calc.evaluate("8*3/4+2") == "8.0"

def test_deep_parentheses_1(calc):
    assert calc.evaluate("((2+3)*(4-1))") == "15"

def test_deep_parentheses_2(calc):
    assert calc.evaluate("(((1+1)+1)+1)") == "4"

def test_nested_mixed(calc):
    assert calc.evaluate("(2+(3*4))-5") == "9"

def test_nested_mixed_2(calc):
    assert calc.evaluate("((10/2)+(3*2))") == "11.0"

def test_long_expression(calc):
    assert calc.evaluate("1+2+3+4+5+6+7+8+9") == "45"


# =====================================================
# 11–20: Floating Point Precision
# =====================================================

def test_float_precision_1(calc):
    assert calc.evaluate("0.1+0.2") == str(0.1+0.2)

def test_float_precision_2(calc):
    assert calc.evaluate("1.333*3") == str(1.333*3)

def test_small_numbers(calc):
    assert calc.evaluate("0.0001+0.0002") == str(0.0001+0.0002)

def test_large_float(calc):
    assert calc.evaluate("123456.789*2") == str(123456.789*2)

def test_float_division(calc):
    assert calc.evaluate("5/2") == "2.5"

def test_float_negative(calc):
    assert calc.evaluate("-2.5*2") == "-5.0"

def test_float_complex(calc):
    assert calc.evaluate("2.5*3.2-1.1") == str(2.5*3.2-1.1)

def test_float_chain(calc):
    assert calc.evaluate("1.1+2.2+3.3") == str(1.1+2.2+3.3)

def test_scientific_notation(calc):
    assert calc.evaluate("1e3+2") == "1002.0"

def test_scientific_negative(calc):
    assert calc.evaluate("1e-3") == "0.001"


# =====================================================
# 21–30: Error Handling & Invalid Syntax
# =====================================================

def test_double_operator(calc):
    assert calc.evaluate("5**") == "Error"

def test_triple_operator(calc):
    assert calc.evaluate("5+++3") == "Error"

def test_unmatched_parenthesis_1(calc):
    assert calc.evaluate("(5+3") == "Error"

def test_unmatched_parenthesis_2(calc):
    assert calc.evaluate("5+3)") == "Error"

def test_empty_string(calc):
    assert calc.evaluate("") == "Error"

def test_only_operator(calc):
    assert calc.evaluate("+") == "Error"

def test_space_input(calc):
    assert calc.evaluate("   ") == "Error"

def test_text_input(calc):
    assert calc.evaluate("hello") == "Error"

def test_invalid_symbols(calc):
    assert calc.evaluate("5$3") == "Error"

def test_divide_by_zero(calc):
    assert calc.evaluate("100/0") == "Error"


# =====================================================
# 31–40: Security / Injection Edge Cases (eval risks)
# =====================================================

def test_eval_injection_import(calc):
    assert calc.evaluate("__import__('os')") == "Error"

def test_eval_injection_system(calc):
    assert calc.evaluate("__import__('os').system('ls')") == "Error"

def test_eval_lambda(calc):
    assert calc.evaluate("(lambda x: x)(5)") == "Error"

def test_eval_exec(calc):
    assert calc.evaluate("exec('print(5)')") == "Error"

def test_eval_attribute_access(calc):
    assert calc.evaluate("(1).__class__") == "Error"

def test_eval_globals(calc):
    assert calc.evaluate("globals()") == "Error"

def test_eval_locals(calc):
    assert calc.evaluate("locals()") == "Error"

def test_eval_open(calc):
    assert calc.evaluate("open('file.txt')") == "Error"

def test_eval_list(calc):
    assert calc.evaluate("[1,2,3]") == "Error"

def test_eval_dict(calc):
    assert calc.evaluate("{1:2}") == "Error"


# =====================================================
# 41–50: Square & Square Root Extreme Cases
# =====================================================

def test_square_large(calc):
    assert calc.square("1000000") == "1000000000000.0"

def test_square_zero(calc):
    assert calc.square("0") == "0.0"

def test_square_negative_large(calc):
    assert calc.square("-10000") == "100000000.0"

def test_square_invalid(calc):
    assert calc.square("abc") == "Error"

def test_sqrt_zero(calc):
    assert calc.sqrt("0") == "0.0"

def test_sqrt_large(calc):
    assert calc.sqrt("1000000") == "1000.0"

def test_sqrt_fraction(calc):
    assert calc.sqrt("0.25") == "0.5"

def test_sqrt_negative(calc):
    assert calc.sqrt("-16") == "Error"

def test_sqrt_invalid(calc):
    assert calc.sqrt("xyz") == "Error"

def test_sqrt_scientific(calc):
    assert calc.sqrt("1e4") == "100.0"
