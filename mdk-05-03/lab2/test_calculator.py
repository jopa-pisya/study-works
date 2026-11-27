import unittest
import calculator as calc

# Обозначения в комментариях к тестам:
#   Уровень:  модульный (unit) / интеграционный (integration)
#   Характер: позитивный (корректные данные) / негативный (некорректные данные)
#   Ящик:     чёрный (только входы и выходы) / белый (знаем код и ветки) /
#             серый (часть внутреннего устройства известна)


class TestAdd(unittest.TestCase):
    # Модульный, позитивный, чёрный ящик.
    # Обычный пример: проверяем результат сложения по входным данным.
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    # Модульный, позитивный, чёрный ящик.
    # Отрицательные числа — допустимые данные, поэтому тест позитивный.
    def test_add_negative(self):
        self.assertEqual(calc.add(-2, 5), 3)


class TestSub(unittest.TestCase):
    # Модульный, позитивный, чёрный ящик.
    # Обычное вычитание: 10 - 4 = 6.
    def test_sub(self):
        self.assertEqual(calc.sub(10, 4), 6)

    # Модульный, позитивный, чёрный ящик.
    # Проверяем, что при вычитании большего из меньшего результат отрицательный.
    def test_sub_negative(self):
        self.assertEqual(calc.sub(4, 10), -6)


class TestMul(unittest.TestCase):
    # Модульный, позитивный, чёрный ящик.
    # Обычное умножение: 6 * 7 = 42.
    def test_mul(self):
        self.assertEqual(calc.mul(6, 7), 42)

    # Модульный, позитивный, чёрный ящик.
    # Граничное (особое) значение: умножение на 0 всегда даёт 0.
    def test_mul_zero(self):
        self.assertEqual(calc.mul(15, 0), 0)


class TestDiv(unittest.TestCase):
    # Модульный, позитивный, чёрный ящик.
    # Обычное деление нацело: 10 / 2 = 5.
    def test_div(self):
        self.assertEqual(calc.div(10, 2), 5)

    # Модульный, позитивный, чёрный ящик.
    # Деление с дробным результатом: 5 / 2 = 2.5.
    def test_div_float(self):
        self.assertEqual(calc.div(5, 2), 2.5)

    # Модульный, негативный, белый ящик.
    # Недопустимые данные (деление на 0). Тест знает про ветку if b == 0
    # и про то, что функция возвращает строку "Ошибка", а не исключение.
    def test_div_zero(self):
        self.assertEqual(calc.div(5, 0), "Ошибка")


class TestPower(unittest.TestCase):
    # Модульный, позитивный, чёрный ящик.
    # Обычное возведение в степень: 2 ** 3 = 8.
    def test_power(self):
        self.assertEqual(calc.power(2, 3), 8)

    # Модульный, позитивный, чёрный ящик.
    # Граничное значение: любое число в степени 0 равно 1.
    def test_power_zero(self):
        self.assertEqual(calc.power(5, 0), 1)


class TestSqrt(unittest.TestCase):
    # Модульный, позитивный, чёрный ящик.
    # Корень из полного квадрата: sqrt(9) = 3.
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(9), 3)

    # Модульный, позитивный, чёрный ящик.
    # Корень из дробного числа: sqrt(2.25) = 1.5.
    def test_sqrt_float(self):
        self.assertEqual(calc.sqrt(2.25), 1.5)

    # Модульный, негативный, белый ящик.
    # Недопустимые данные (корень из отрицательного числа).
    # Тест опирается на ветку if a < 0 и возврат строки "Ошибка".
    def test_sqrt_negative(self):
        self.assertEqual(calc.sqrt(-4), "Ошибка")


class TestFactorial(unittest.TestCase):
    # Модульный, позитивный, чёрный ящик.
    # Граничный случай: 0! = 1.
    def test_factorial_zero(self):
        self.assertEqual(calc.factorial(0), 1)

    # Модульный, позитивный, чёрный ящик.
    # Обычный случай: 5! = 120.
    def test_factorial(self):
        self.assertEqual(calc.factorial(5), 120)

    # Модульный, негативный, белый ящик.
    # Недопустимые данные (факториал отрицательного числа).
    # Тест опирается на ветку if n < 0 и возврат строки "Ошибка".
    def test_factorial_negative(self):
        self.assertEqual(calc.factorial(-3), "Ошибка")


class TestMemory(unittest.TestCase):
    # Перед каждым тестом сбрасываем глобальную память калькулятора,
    # чтобы тесты не влияли друг на друга.
    def setUp(self):
        calc.memory_clear()

    # Модульный, позитивный, серый ящик.
    # Знаем, что память хранится в глобальной переменной,
    # но работаем только через публичные функции.
    def test_memory_empty(self):
        self.assertEqual(calc.memory_get(), 0)

    # Модульный, позитивный, серый ящик.
    # Сохранение значения в память и чтение его обратно.
    def test_memory_save(self):
        calc.memory_save(25)
        self.assertEqual(calc.memory_get(), 25)

    # Модульный, позитивный, серый ящик.
    # Прибавление к уже сохранённому значению: 10 + 5 = 15.
    def test_memory_add(self):
        calc.memory_save(10)
        calc.memory_add(5)
        self.assertEqual(calc.memory_get(), 15)

    # Модульный, позитивный, серый ящик.
    # После очистки память должна снова стать 0.
    def test_memory_clear(self):
        calc.memory_save(7)
        calc.memory_clear()
        self.assertEqual(calc.memory_get(), 0)


class TestTogether(unittest.TestCase):
    # Интеграционный, позитивный, серый ящик.
    # Проверяем совместную работу двух функций: (2 + 3) * 4 = 20.
    # Результат add передаётся в mul — это уже взаимодействие модулей.
    def test_chain(self):
        result = calc.add(2, 3)
        result = calc.mul(result, 4)
        self.assertEqual(result, 20)

    # Интеграционный, позитивный, серый ящик.
    # Совместная работа памяти и арифметики:
    # сохраняем (10 + 5) = 15 в память, затем 15 * 2 = 30.
    def test_memory_and_calc(self):
        calc.memory_save(calc.add(10, 5))
        result = calc.mul(calc.memory_get(), 2)
        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main()
