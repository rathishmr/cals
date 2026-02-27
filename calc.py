import ast
import operator
import tkinter as tk


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


# ------------------ UI ------------------

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:
    def __init__(self):
        self.logic = CalculatorLogic()

        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "÷", "*": "×", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons_frame()

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    # ------------------ BUTTON LOGIC ------------------

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def square(self):
        result = self.logic.evaluate(f"{self.current_expression}**2")
        self.current_expression = result
        self.update_label()

    def sqrt(self):
        result = self.logic.evaluate(f"{self.current_expression}**0.5")
        self.current_expression = result
        self.update_label()

    def evaluate(self):
        expression = self.current_expression
        result = self.logic.evaluate(expression)
        self.current_expression = result
        self.total_expression = ""
        self.update_label()

    # ------------------ UI BUILD ------------------

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")

        for x in range(5):
            frame.rowconfigure(x, weight=1)
            frame.columnconfigure(x, weight=1)

        return frame

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),
                               font=DIGITS_FONT_STYLE,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol,
                               font=DEFAULT_FONT_STYLE,
                               command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_special_buttons(self):
        tk.Button(self.buttons_frame, text="C",
                  font=DEFAULT_FONT_STYLE,
                  command=self.clear).grid(row=0, column=1, sticky=tk.NSEW)

        tk.Button(self.buttons_frame, text="=",
                  font=DEFAULT_FONT_STYLE,
                  command=self.evaluate).grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

        tk.Button(self.buttons_frame, text="x²",
                  font=DEFAULT_FONT_STYLE,
                  command=self.square).grid(row=0, column=2, sticky=tk.NSEW)

        tk.Button(self.buttons_frame, text="√x",
                  font=DEFAULT_FONT_STYLE,
                  command=self.sqrt).grid(row=0, column=3, sticky=tk.NSEW)

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()

