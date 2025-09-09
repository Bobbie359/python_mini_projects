                                                #######
import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return math.pow(a, b)

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import messagebox

    calc = Calculator()

    def calculate():
        op = operation.get()
        try:
            a = float(entry_a.get())
            b = float(entry_b.get()) if op != "sqrt" else None
            if op == "add":
                result = calc.add(a, b)
            elif op == "subtract":
                result = calc.subtract(a, b)
            elif op == "multiply":
                result = calc.multiply(a, b)
            elif op == "divide":
                result = calc.divide(a, b)
            elif op == "power":
                result = calc.power(a, b)
            elif op == "sqrt":
                result = calc.sqrt(a)
            else:
                result = "Invalid operation"
            result_label.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    root = tk.Tk()
    root.title("Calculator")

    tk.Label(root, text="First Number:").grid(row=0, column=0)
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1)

    tk.Label(root, text="Second Number:").grid(row=1, column=0)
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1)

    tk.Label(root, text="Operation:").grid(row=2, column=0)
    operation = tk.StringVar(value="add")
    ops = ["add", "subtract", "multiply", "divide", "power", "sqrt"]
    tk.OptionMenu(root, operation, *ops).grid(row=2, column=1)

    tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2)
    result_label = tk.Label(root, text="Result:")
    result_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()
