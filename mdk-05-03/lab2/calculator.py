# Функции калькулятора

memory = 0


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Ошибка"
    return a / b


def power(a, b):
    return a ** b


def sqrt(a):
    if a < 0:
        return "Ошибка"
    return a ** 0.5


def factorial(n):
    if n < 0 or n != int(n):
        return "Ошибка"
    result = 1
    for i in range(1, int(n) + 1):
        result = result * i
    return result


def memory_save(x):
    global memory
    memory = x


def memory_get():
    return memory


def memory_add(x):
    global memory
    memory = memory + x


def memory_clear():
    global memory
    memory = 0
