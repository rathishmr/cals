import ast
import operator
import math

# ------------------ LOGIC ------------------

class CalculatorLogic:

    OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
    }

    def evaluate(self, expression: str) -> str:
        try:
            parsed = ast.parse(expression, mode="eval")

            # 🚨 HARD SECURITY BLOCK
            for node in ast.walk(parsed):
                if isinstance(node, (
                    ast.Call,
                    ast.Attribute,
                    ast.Name,
                    ast.Lambda,
                    ast.Import,
                    ast.ImportFrom,
                )):
                    return "Error"

            result = self._safe_eval(parsed.body)
            return str(result)

        except Exception:
            return "Error"

    def _safe_eval(self, node):

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError

        elif isinstance(node, ast.BinOp):
            if type(node.op) not in self.OPERATORS:
                raise ValueError

            left = self._safe_eval(node.left)
            right = self._safe_eval(node.right)

            return self.OPERATORS[type(node.op)](left, right)

        elif isinstance(node, ast.UnaryOp):
            if type(node.op) not in self.OPERATORS:
                raise ValueError

            operand = self._safe_eval(node.operand)
            return self.OPERATORS[type(node.op)](operand)

        else:
            raise ValueError

    def square(self, value: str) -> str:
        try:
            num = float(value)
            return str(num ** 2)
        except Exception:
            return "Error"

    def sqrt(self, value: str) -> str:
        try:
            num = float(value)
            if num < 0:
                return "Error"
            return str(math.sqrt(num))
        except Exception:
            return "Error"


