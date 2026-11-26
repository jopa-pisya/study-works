import tkinter as tk
import calculator as calc

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x420")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

first = None
action = None


def show(value):
    entry.delete(0, tk.END)
    if isinstance(value, float) and value.is_integer():
        value = int(value)
    entry.insert(0, str(value))


def digit(d):
    if entry.get() == "Ошибка":
        entry.delete(0, tk.END)
    entry.insert(tk.END, d)


def dot():
    if entry.get() == "Ошибка":
        entry.delete(0, tk.END)
    if "." not in entry.get():
        entry.insert(tk.END, ".")


def clear():
    global first, action
    first = None
    action = None
    entry.delete(0, tk.END)


def operation(op):
    global first, action
    if entry.get() == "" or entry.get() == "Ошибка":
        return
    first = float(entry.get())
    action = op
    entry.delete(0, tk.END)


def equals():
    global action
    if action is None or entry.get() == "":
        return
    second = float(entry.get())
    if action == "+":
        result = calc.add(first, second)
    elif action == "-":
        result = calc.sub(first, second)
    elif action == "*":
        result = calc.mul(first, second)
    elif action == "/":
        result = calc.div(first, second)
    else:
        result = calc.power(first, second)
    show(result)
    action = None


def unary(op):
    if entry.get() == "" or entry.get() == "Ошибка":
        return
    number = float(entry.get())
    if op == "sqrt":
        show(calc.sqrt(number))
    else:
        show(calc.factorial(number))


def memory(op):
    if op == "MS" and entry.get() not in ("", "Ошибка"):
        calc.memory_save(float(entry.get()))
    elif op == "MR":
        show(calc.memory_get())
    elif op == "M+" and entry.get() not in ("", "Ошибка"):
        calc.memory_add(float(entry.get()))
    elif op == "MC":
        calc.memory_clear()


buttons = [
    ("7", 1, 0, lambda: digit("7")),
    ("8", 1, 1, lambda: digit("8")),
    ("9", 1, 2, lambda: digit("9")),
    ("/", 1, 3, lambda: operation("/")),
    ("4", 2, 0, lambda: digit("4")),
    ("5", 2, 1, lambda: digit("5")),
    ("6", 2, 2, lambda: digit("6")),
    ("*", 2, 3, lambda: operation("*")),
    ("1", 3, 0, lambda: digit("1")),
    ("2", 3, 1, lambda: digit("2")),
    ("3", 3, 2, lambda: digit("3")),
    ("-", 3, 3, lambda: operation("-")),
    ("0", 4, 0, lambda: digit("0")),
    (".", 4, 1, dot),
    ("=", 4, 2, equals),
    ("+", 4, 3, lambda: operation("+")),
    ("√", 5, 0, lambda: unary("sqrt")),
    ("x^y", 5, 1, lambda: operation("^")),
    ("n!", 5, 2, lambda: unary("fact")),
    ("C", 5, 3, clear),
    ("MS", 6, 0, lambda: memory("MS")),
    ("MR", 6, 1, lambda: memory("MR")),
    ("M+", 6, 2, lambda: memory("M+")),
    ("MC", 6, 3, lambda: memory("MC")),
]

for text, row, column, command in buttons:
    tk.Button(root, text=text, font=("Arial", 14), command=command).grid(
        row=row, column=column, sticky="nsew", padx=2, pady=2
    )

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(7):
    root.rowconfigure(i, weight=1)

if __name__ == "__main__":
    root.mainloop()
