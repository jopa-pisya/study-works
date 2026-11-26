import unittest
import calculator as calc


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(calc.add(-2, 5), 3)


class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(calc.sub(10, 4), 6)

    def test_sub_negative(self):
        self.assertEqual(calc.sub(4, 10), -6)


class TestMul(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(calc.mul(6, 7), 42)

    def test_mul_zero(self):
        self.assertEqual(calc.mul(15, 0), 0)


class TestDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(calc.div(10, 2), 5)

    def test_div_float(self):
        self.assertEqual(calc.div(5, 2), 2.5)

    def test_div_zero(self):
        self.assertEqual(calc.div(5, 0), "Ошибка")


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(calc.power(2, 3), 8)

    def test_power_zero(self):
        self.assertEqual(calc.power(5, 0), 1)


class TestSqrt(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(9), 3)

    def test_sqrt_float(self):
        self.assertEqual(calc.sqrt(2.25), 1.5)

    def test_sqrt_negative(self):
        self.assertEqual(calc.sqrt(-4), "Ошибка")


class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(calc.factorial(0), 1)

    def test_factorial(self):
        self.assertEqual(calc.factorial(5), 120)

    def test_factorial_negative(self):
        self.assertEqual(calc.factorial(-3), "Ошибка")


class TestMemory(unittest.TestCase):
    def setUp(self):
        calc.memory_clear()

    def test_memory_empty(self):
        self.assertEqual(calc.memory_get(), 0)

    def test_memory_save(self):
        calc.memory_save(25)
        self.assertEqual(calc.memory_get(), 25)

    def test_memory_add(self):
        calc.memory_save(10)
        calc.memory_add(5)
        self.assertEqual(calc.memory_get(), 15)

    def test_memory_clear(self):
        calc.memory_save(7)
        calc.memory_clear()
        self.assertEqual(calc.memory_get(), 0)


class TestTogether(unittest.TestCase):
    def test_chain(self):
        result = calc.add(2, 3)
        result = calc.mul(result, 4)
        self.assertEqual(result, 20)

    def test_memory_and_calc(self):
        calc.memory_save(calc.add(10, 5))
        result = calc.mul(calc.memory_get(), 2)
        self.assertEqual(result, 30)


if __name__ == "__main__":
    unittest.main()
