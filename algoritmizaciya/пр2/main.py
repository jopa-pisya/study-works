"""
Практическая работа № 2.

Междисциплинарный курс «Основы алгоритмизации и программирования»,
раздел «Объектно-ориентированное программирование»,
тема 1.2 «Классы и объекты в языке Python».

Тема работы: «Объявление класса, создание экземпляров класса».

Модуль содержит решения заданий 1–18 (обязательный минимум) и
заданий 19–20 (повышенная сложность). Каждое задание отделено
комментарием с номером и оформлено по стандарту PEP 8.

Запуск всех заданий:      python main.py
Запуск одного задания:    python main.py 7
"""

import math
import sys
import weakref

# ======================================================================
# ЗАДАНИЕ 1. Класс Point (точка на плоскости)
# ======================================================================


class Point:
    """Точка на плоскости с публичными координатами x и y."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        """Вернуть расстояние до другой точки other."""
        return math.hypot(other.x - self.x, other.y - self.y)

    def __str__(self):
        """Строковое представление вида Point (2; 3)."""
        return f"Point ({self.x}; {self.y})"


def task_01():
    """Задание 1: два экземпляра Point и расстояние между ними."""
    a = Point(0, 0)
    b = Point(3, 4)

    print("Первая точка: ", a)
    print("Вторая точка: ", b)
    print(f"Расстояние a -> b: {a.distance_to(b)}")
    print(f"Расстояние b -> a: {b.distance_to(a)}")
    print("Расстояние не зависит от направления:",
          a.distance_to(b) == b.distance_to(a))


# ======================================================================
# ЗАДАНИЕ 2. Класс Person с проверкой возраста
# ======================================================================


class Person:
    """Человек с именем и возрастом, проверяемым в инициализаторе."""

    def __init__(self, name, age):
        if not 0 < age <= 120:
            raise ValueError(
                f"Недопустимый возраст {age}: должно быть 0 < age <= 120"
            )
        self.name = name
        self.age = age

    def greet(self):
        """Вернуть строку приветствия."""
        return f"Привет, я {self.name}, мне {self.age} лет."

    def __str__(self):
        return f"{self.name}, {self.age} лет"


def task_02():
    """Задание 2: три приветствия и перехват ValueError."""
    people = [
        Person("Анна", 19),
        Person("Пётр", 25),
        Person("Мария", 41),
    ]

    for person in people:
        print(person.greet())

    try:
        Person("Иван", 150)
    except ValueError as error:
        print(f"Ошибка при создании Person: {error}")


# ======================================================================
# ЗАДАНИЕ 3. Класс Car и работа с атрибутами объекта
# ======================================================================


class Car:
    """Автомобиль: бренд, модель, год выпуска."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        """Вернуть краткую информацию об автомобиле."""
        return f"{self.brand} {self.model}, {self.year} г."

    def __str__(self):
        return f"Автомобиль: {self.info()}"


def task_03():
    """Задание 3: изменение, добавление и удаление атрибутов."""
    car1 = Car("Lada", "Vesta", 2018)
    car2 = Car("Toyota", "Camry", 2020)

    print(car1)
    print(car2)
    print("Метод info():", car2.info())

    print("\n--- Меняем год выпуска первого автомобиля ---")
    car1.year = 2021
    print(car1)

    print("\n--- Добавляем атрибут color второму автомобилю ---")
    print("hasattr(car2, 'color') до добавления:", hasattr(car2, "color"))
    car2.color = "белый"
    print("hasattr(car2, 'color') после добавления:", hasattr(car2, "color"))
    print("Цвет:", car2.color)

    print("\n--- Удаляем атрибут color ---")
    del car2.color
    print("hasattr(car2, 'color') после удаления:", hasattr(car2, "color"))
    try:
        print(car2.color)
    except AttributeError as error:
        print("Обращение к удалённому атрибуту:", error)

    # Вывод: атрибуты в Python не описываются заранее, а создаются в момент
    # присваивания и хранятся в словаре объекта __dict__. Именно поэтому
    # атрибут можно добавить и удалить у отдельного экземпляра, не меняя
    # сам класс: у car1 атрибута color нет, у car2 он появлялся и исчезал.
    print("\nАтрибуты car2:", sorted(car2.__dict__))
    print("Атрибуты car1:", sorted(car1.__dict__))


# ======================================================================
# ЗАДАНИЕ 4. Класс Student со списком оценок
# ======================================================================


class Student:
    """Студент с именем, группой и списком оценок."""

    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = list(grades)

    def average(self):
        """Вернуть средний балл; для пустого списка оценок — 0.0."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} ({self.group}), средний балл {self.average():.2f}"


def task_04():
    """Задание 4: средние баллы трёх студентов и isinstance()."""
    students = [
        Student("Анна", "П-21", [5, 4, 5, 5]),
        Student("Пётр", "П-21", [4, 3, 4, 4]),
        Student("Мария", "П-22", []),
    ]

    for student in students:
        print(f"{student.name}: {student.average():.2f}")

    print("\nПроверка isinstance():")
    print("isinstance(students[0], Student):",
          isinstance(students[0], Student))
    print("isinstance('строка', Student):", isinstance("строка", Student))
    print("isinstance(42, Student):", isinstance(42, Student))


# ======================================================================
# ЗАДАНИЕ 5. Пустой класс как именованный контейнер
# ======================================================================


class EmptyBox:
    """Пустой класс-контейнер: тело состоит только из pass."""

    pass


def task_05():
    """Задание 5: динамическое добавление атрибутов в пустой класс."""
    box = EmptyBox()
    box.owner = "Иван"
    box.items = 3

    print("Владелец:", box.owner)
    print("Количество предметов:", box.items)
    print("Словарь атрибутов объекта:", box.__dict__)

    # Вывод: приём работает потому, что у объекта есть собственный словарь
    # __dict__, и присваивание box.owner = 'Иван' создаёт в нём запись.
    # Класс при этом остаётся пустым: EmptyBox.owner не существует.
    # Такой приём оправдан для простых записей данных (результат запроса,
    # настройки, «мешок» значений), когда полноценный класс с методами
    # избыточен, а словарь неудобен из-за обращения по строковому ключу.
    print("Есть ли owner у самого класса:",
          hasattr(EmptyBox, "owner"))


# ======================================================================
# ЗАДАНИЕ 6. Класс Circle с вычисляемыми методами
# ======================================================================


class Circle:
    """Круг с радиусом и вычисляемыми площадью и периметром."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Площадь круга."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Длина окружности."""
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Круг радиуса {self.radius}: площадь {self.area():.2f}"


def task_06():
    """Задание 6: три круга, их площади и периметры."""
    for radius in (1.0, 2.5, 10.0):
        circle = Circle(radius)
        print(circle)
        print(f"  периметр: {circle.perimeter():.2f}")


# ======================================================================
# ЗАДАНИЕ 7. Класс Rectangle и поиск максимума по площади
# ======================================================================


class Rectangle:
    """Прямоугольник с шириной и высотой."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Площадь прямоугольника."""
        return self.width * self.height

    def perimeter(self):
        """Периметр прямоугольника."""
        return 2 * (self.width + self.height)

    def is_square(self):
        """Вернуть True, если прямоугольник является квадратом."""
        return self.width == self.height

    def __str__(self):
        kind = "квадрат" if self.is_square() else "прямоугольник"
        return (f"{kind} {self.width}x{self.height}: "
                f"площадь {self.area()}, периметр {self.perimeter()}")


def task_07():
    """Задание 7: максимум по площади и количество квадратов."""
    rects = [
        Rectangle(3, 4),
        Rectangle(5, 5),
        Rectangle(10, 2),
        Rectangle(4, 4),
        Rectangle(6, 7),
    ]

    for rect in rects:
        print(rect)

    biggest = max(rects, key=lambda r: r.area())
    print("\nМаксимальная площадь:", biggest)

    squares = sum(1 for rect in rects if rect.is_square())
    print("Количество квадратов в списке:", squares)


# ======================================================================
# ЗАДАНИЕ 8. Атрибут класса — счётчик точек
# ======================================================================


class PointCounter(Point):
    """Класс Point из задания 1, дополненный счётчиком count_points."""

    count_points = 0

    def __init__(self, x, y):
        super().__init__(x, y)
        PointCounter.count_points += 1


def task_08():
    """Задание 8: счётчик созданных точек и атрибут экземпляра."""
    p1 = PointCounter(1, 2)
    print(f"Создана {p1}, PointCounter.count_points = "
          f"{PointCounter.count_points}")

    p2 = PointCounter(3, 4)
    print(f"Создана {p2}, PointCounter.count_points = "
          f"{PointCounter.count_points}")

    p3 = PointCounter(5, 6)
    print(f"Создана {p3}, PointCounter.count_points = "
          f"{PointCounter.count_points}")

    print("\n--- Атрибут экземпляра ---")
    p1.color = "red"
    print("p1.color =", p1.color)
    print("hasattr(p2, 'color'):", hasattr(p2, "color"))
    print("hasattr(PointCounter, 'color'):", hasattr(PointCounter, "color"))
    print("PointCounter.count_points =", PointCounter.count_points)

    # Вывод (см. таблицу 2 методических указаний): count_points объявлен
    # в теле класса, поэтому он один на всех и меняется через
    # PointCounter.count_points += 1. Присваивание p1.color = 'red'
    # создаёт атрибут только у объекта p1: p2 и сам класс его не видят.
    # Если бы в __init__ было написано self.count_points += 1, то после
    # первого же объекта у него появился бы собственный атрибут, и общий
    # счётчик перестал бы увеличиваться — поэтому обращаемся к классу.


# ======================================================================
# ЗАДАНИЕ 9. Счётчик живых экземпляров и метод __del__
# ======================================================================


class Counter:
    """Счётчик живых экземпляров: демонстрация метода __del__."""

    instances = 0

    def __init__(self, name):
        self.name = name
        Counter.instances += 1
        print(f"Создан {self.name}; живых экземпляров: {Counter.instances}")

    def __del__(self):
        Counter.instances -= 1
        print(f"Удалён {self.name}; живых экземпляров: {Counter.instances}")


def task_09():
    """Задание 9: рост и уменьшение счётчика при удалении объекта."""
    c1 = Counter("объект-1")
    c2 = Counter("объект-2")
    c3 = Counter("объект-3")

    print("\nCounter.instances после создания трёх объектов:",
          Counter.instances)

    print("\nУдаляем объект-2 функцией del")
    del c2
    print("Counter.instances после удаления:", Counter.instances)

    # Вывод: __del__ — деструктор. Он вызывается автоматически, когда на
    # объект больше не остаётся ссылок (в CPython — сразу после del по
    # счётчику ссылок, иначе — сборщиком мусора). В этот момент объект ещё
    # существует, поэтому в __del__ доступны его атрибуты, и счётчик
    # успевает уменьшиться до фактического освобождения памяти.
    print("\nЖивые объекты:", c1.name, "и", c3.name)


# ======================================================================
# ЗАДАНИЕ 10. Класс Temperature: __str__ и __repr__
# ======================================================================


class Temperature:
    """Температура в градусах Цельсия: __str__ и __repr__."""

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        """Перевести температуру в градусы Фаренгейта."""
        return self.celsius * 9 / 5 + 32

    def __repr__(self):
        """Представление для разработчика."""
        return f"Temperature({self.celsius:.1f})"

    def __str__(self):
        """Представление для пользователя."""
        return f"{self.celsius:.1f} °C"


def task_10():
    """Задание 10: разница между print(t) и repr(t)."""
    t = Temperature(20.0)

    print("print(t):      ", t)
    print("repr(t):       ", repr(t))
    print("print([t]):     список печатается через __repr__ ->", [t])
    print(f"В градусах Фаренгейта: {t.to_fahrenheit():.1f} °F")

    # Вывод: print() и f-строки используют __str__ — «человеческое»
    # представление (20.0 °C). repr() и контейнеры используют __repr__ —
    # однозначное представление, по которому видно, как объект создан
    # (Temperature(20.0)). __str__ — для пользователя, __repr__ — для
    # разработчика и отладки.


# ======================================================================
# ЗАДАНИЕ 11. Temperature 2.0: приватное значение и свойство fahrenheit
# ======================================================================


class TemperatureV2:
    """Версия класса Temperature с приватным __celsius и свойством."""

    def __init__(self, celsius=0.0):
        self.__celsius = float(celsius)

    @property
    def celsius(self):
        """Температура в градусах Цельсия (только чтение)."""
        return self.__celsius

    @property
    def fahrenheit(self):
        """Температура в градусах Фаренгейта."""
        return self.__celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.__celsius = (value - 32) * 5 / 9

    def __str__(self):
        return f"{self.__celsius:.1f} °C ({self.fahrenheit:.1f} °F)"


def task_11():
    """Задание 11: двустороннее свойство и защита приватного атрибута."""
    t = TemperatureV2(20.0)
    print("t.celsius   =", round(t.celsius, 2))
    print("t.fahrenheit =", round(t.fahrenheit, 2))

    print("\nУстанавливаем t.fahrenheit = 68")
    t.fahrenheit = 68
    print("t.celsius   =", round(t.celsius, 2))
    print("t.fahrenheit =", round(t.fahrenheit, 2))
    print("Обратное преобразование корректно:", round(t.celsius, 2) == 20.0)

    print("\nПопытка прямой записи через свойство celsius:")
    try:
        t.celsius = 25
    except AttributeError as error:
        print("AttributeError:", error)

    print("\nПопытка прочитать приватный атрибут извне класса:")
    try:
        print(getattr(t, "__celsius"))
    except AttributeError as error:
        print("AttributeError:", error)
    print("Реальное имя после name mangling хранит значение:",
          round(t._TemperatureV2__celsius, 2))

    # Замечание: присваивание t.__celsius = 100, выполненное ВНЕ тела
    # класса, не изменит состояние объекта — оно создаст новый посторонний
    # атрибут с именем __celsius, потому что name mangling действует
    # только внутри класса. Настоящее значение лежит в
    # _TemperatureV2__celsius и остаётся недоступным через публичный
    # интерфейс, кроме свойства celsius.
    t.__celsius = 100
    print("После t.__celsius = 100 значение t.celsius не изменилось:",
          round(t.celsius, 2))


# ======================================================================
# ЗАДАНИЕ 12. Класс Wallet: свойство с валидацией
# ======================================================================


class Wallet:
    """Кошелёк с приватным балансом и свойством money."""

    def __init__(self, money=0):
        if money < 0:
            raise ValueError("Отрицательная сумма")
        self.__money = money

    @property
    def money(self):
        """Текущая сумма в кошельке (только чтение)."""
        return self.__money

    @money.setter
    def money(self, value):
        if value < 0:
            raise ValueError("Отрицательная сумма")
        self.__money = value

    def withdraw(self, amount):
        """Снять amount рублей с проверками суммы и остатка."""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__money:
            raise ValueError("Недостаточно средств")
        self.__money -= amount
        return self.__money

    def __str__(self):
        return f"Кошелёк: {self.__money} руб."


def task_12():
    """Задание 12: property с валидацией и обе ошибки через try/except."""
    w = Wallet(100)
    print("Начальный баланс (property):", w.money)

    w.money = 150
    print("После w.money = 150:", w.money)

    print("Снимаем 50 руб., остаток:", w.withdraw(50))

    try:
        w.money = -10
    except ValueError as error:
        print("ValueError при w.money = -10:", error)

    try:
        w.withdraw(1000)
    except ValueError as error:
        print("ValueError при w.withdraw(1000):", error)

    try:
        w.withdraw(-5)
    except ValueError as error:
        print("ValueError при w.withdraw(-5):", error)

    print("\nПриватный атрибут после name mangling: w._Wallet__money =",
          w._Wallet__money)
    # Вывод: __money превращается интерпретатором в _Wallet__money. Именно
    # по этому имени значение и хранится, а обращение w.__money извне
    # класса к реальному состоянию не приводит.


# ======================================================================
# ЗАДАНИЕ 13. Класс BankAccount с историей операций
# ======================================================================


class BankAccount:
    """Банковский счёт с защищённым балансом и историей операций."""

    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.owner = owner
        self.__balance = float(balance)
        self.__history = []

    @property
    def balance(self):
        """Текущий баланс (только чтение)."""
        return self.__balance

    def deposit(self, amount):
        """Положить amount рублей на счёт."""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.__balance += amount
        self.__history.append(f"+{amount:.2f}")

    def withdraw(self, amount):
        """Снять amount рублей со счёта."""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
        self.__history.append(f"-{amount:.2f}")

    def show_history(self):
        """Напечатать историю операций."""
        print(f"История операций счёта {self.owner}:")
        for record in self.__history:
            print("  ", record)

    def __str__(self):
        return f"Счёт ({self.owner}): {self.__balance:.2f} руб."


def task_13():
    """Задание 13: операции, история и обработка двух ошибок."""
    acc = BankAccount("Иванов И. И.", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    acc.deposit(120.50)

    print(acc)
    print("Баланс через свойство:", acc.balance)
    acc.show_history()

    print()
    try:
        acc.deposit(-100)
    except ValueError as error:
        print("ValueError при acc.deposit(-100):", error)

    try:
        acc.withdraw(100000)
    except ValueError as error:
        print("ValueError при acc.withdraw(100000):", error)


# ======================================================================
# ЗАДАНИЕ 14. Класс Book с приватным флагом доступности
# ======================================================================


class Book:
    """Книга с приватным флагом доступности."""

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.__is_available = True

    @property
    def is_available(self):
        """True, если книга находится в фонде."""
        return self.__is_available

    def take(self):
        """Выдать книгу; вернуть True при успехе."""
        if not self.__is_available:
            print(f"Книга «{self.title}» уже выдана")
            return False
        self.__is_available = False
        print(f"Книга «{self.title}» выдана")
        return True

    def give_back(self):
        """Вернуть книгу в фонд."""
        if self.__is_available:
            print(f"Книга «{self.title}» уже в фонде")
            return
        self.__is_available = True
        print(f"Книга «{self.title}» возвращена")

    def __str__(self):
        status = "доступна" if self.__is_available else "выдана"
        return f"«{self.title}», {self.author} ({self.pages} с.) — {status}"


def task_14():
    """Задание 14: список книг, выдача двух и список доступных."""
    books = [
        Book("Война и мир", "Л. Н. Толстой", 1274),
        Book("Мёртвые души", "Н. В. Гоголь", 352),
        Book("Мастер и Маргарита", "М. А. Булгаков", 480),
        Book("Преступление и наказание", "Ф. М. Достоевский", 672),
    ]

    print("Все книги:")
    for book in books:
        print(" ", book)

    print("\nВыдаём две книги:")
    books[0].take()
    books[2].take()

    print("\nСостояние после выдачи:")
    for book in books:
        print(" ", book)

    available = [book for book in books if book.is_available]
    print("\nДоступные книги:")
    for book in available:
        print(" ", book.title)

    print("\nПовторная выдача уже выданной книги:")
    books[0].take()


# ======================================================================
# ЗАДАНИЕ 15. Класс Employee: приватная зарплата и повышение
# ======================================================================


class Employee:
    """Сотрудник с приватной зарплатой и методом повышения."""

    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.name = name
        self.__salary = float(salary)

    @property
    def salary(self):
        """Текущая зарплата (только чтение)."""
        return self.__salary

    def raise_salary(self, percent):
        """Увеличить зарплату на percent процентов."""
        if percent <= 0:
            raise ValueError("Процент повышения должен быть положительным")
        self.__salary *= 1 + percent / 100
        return self.__salary

    def __str__(self):
        return f"{self.name}: зарплата {self.__salary:.2f} руб."


def task_15():
    """Задание 15: чтение зарплаты, повышение и отрицательный процент."""
    employee = Employee("Сидоров С. С.", 50000)
    print(employee)
    print("Текущая зарплата:", employee.salary)

    print("\nПовышение на 10 %")
    employee.raise_salary(10)
    print(employee)

    try:
        employee.raise_salary(-5)
    except ValueError as error:
        print("\nValueError при employee.raise_salary(-5):", error)


# ======================================================================
# ЗАДАНИЕ 16. Ведомость по банковским счетам
# ======================================================================


def task_16():
    """Задание 16: агрегатные операции по списку счетов."""
    accounts = [
        BankAccount("ООО «Ромашка»", 300),
        BankAccount("ООО «Лютик»", 1200),
        BankAccount("ИП Петров", 450),
        BankAccount("ООО «Василёк»", 800),
        BankAccount("ИП Смирнова", 150),
    ]

    total = sum(account.balance for account in accounts)
    print(f"Суммарный баланс банка: {total:.2f} руб.")

    richest = max(accounts, key=lambda a: a.balance)
    print("Счёт с максимальным балансом:", richest)

    small = [account for account in accounts if account.balance < 500]
    print("Счетов с балансом менее 500:", len(small))

    print("\nСчета с балансом менее 500:")
    for account in small:
        print(" ", account)


# ======================================================================
# ЗАДАНИЕ 17. Рейтинг студентов
# ======================================================================


def task_17():
    """Задание 17: рейтинг, лучший студент и отличники."""
    students = [
        Student("Иванов", "П-21", [5, 5, 5, 4, 5]),      # 4.80
        Student("Петрова", "П-21", [5, 4, 5, 4]),        # 4.50
        Student("Сидоров", "П-21", [4, 4, 4, 5]),        # 4.25
        Student("Кузнецов", "П-22", [4, 3, 4, 4]),       # 3.75
        Student("Смирнова", "П-22", [5, 5, 5, 5]),       # 5.00
        Student("Орлов", "П-22", [3, 4, 3, 4]),          # 3.50
    ]

    rating = sorted(students, key=lambda s: s.average(), reverse=True)
    print("Рейтинг студентов:")
    for place, student in enumerate(rating, start=1):
        print(f"  {place}. {student.name} — {student.average():.2f}")

    best = max(students, key=lambda s: s.average())
    print("\nЛучший студент:", best.name,
          f"({best.average():.2f})")

    excellent = [student for student in students
                 if student.average() >= 4.5]
    print("Отличники (средний балл не ниже 4.5):",
          ", ".join(student.name for student in excellent))


# ======================================================================
# ЗАДАНИЕ 18. Класс Library — контейнер книг
# ======================================================================


class Library:
    """Библиотека — контейнер объектов Book."""

    def __init__(self, name="Городская библиотека"):
        self.name = name
        self.__books = []

    def add_book(self, book):
        """Добавить книгу; допускаются только объекты Book."""
        if not isinstance(book, Book):
            raise TypeError(
                "В библиотеку можно добавлять только объекты класса Book"
            )
        self.__books.append(book)

    def available_books(self):
        """Вернуть список доступных книг."""
        return [book for book in self.__books if book.is_available]

    def find_by_author(self, author):
        """Найти книги по подстроке фамилии автора без учёта регистра."""
        return [book for book in self.__books
                if author.lower() in book.author.lower()]

    def __str__(self):
        return (f"Библиотека «{self.name}»: всего книг — "
                f"{len(self.__books)}, доступно — "
                f"{len(self.available_books())}")


def task_18():
    """Задание 18: наполнение библиотеки, выдача, поиск и TypeError."""
    library = Library()
    books = [
        Book("Война и мир", "Л. Н. Толстой", 1274),
        Book("Анна Каренина", "Л. Н. Толстой", 864),
        Book("Мёртвые души", "Н. В. Гоголь", 352),
        Book("Мастер и Маргарита", "М. А. Булгаков", 480),
    ]
    for book in books:
        library.add_book(book)

    print(library)

    print("\nВыдаём одну книгу:")
    books[1].take()

    print("\nДоступные книги:")
    for book in library.available_books():
        print(" ", book)

    print("\nПоиск по автору 'толстой' (без учёта регистра):")
    for book in library.find_by_author("толстой"):
        print(" ", book)

    print("\nПоиск по автору 'Гоголь':")
    for book in library.find_by_author("Гоголь"):
        print(" ", book)

    try:
        library.add_book("не книга")
    except TypeError as error:
        print("\nTypeError при добавлении строки:", error)

    print("\nИтог:", library)


# ======================================================================
# ЗАДАНИЕ 19*. Класс Inventory: строгая валидация состояния
# ======================================================================


class Inventory:
    """Инвентарь склада: название товара -> (цена, количество)."""

    def __init__(self):
        self.__items = {}

    def add_item(self, name, price, count):
        """Добавить товар со строгой проверкой типов и значений."""
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой")
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом")
        if isinstance(count, bool) or not isinstance(count, int):
            raise TypeError("Количество должно быть целым числом")
        if price <= 0:
            raise ValueError("Цена должна быть больше нуля")
        if count < 0:
            raise ValueError("Количество не может быть отрицательным")
        self.__items[name] = (float(price), count)

    @property
    def total_value(self):
        """Стоимость всего товара на складе."""
        return sum(price * count for price, count in self.__items.values())

    def search(self, name):
        """Найти товары по частичному совпадению названия."""
        sample = name.lower()
        return {title: data for title, data in self.__items.items()
                if sample in title.lower()}

    def __str__(self):
        lines = [f"Инвентарь: позиций — {len(self.__items)}, "
                 f"стоимость — {self.total_value:.2f} руб."]
        for name, (price, count) in self.__items.items():
            lines.append(f"  {name}: {price:.2f} руб. x {count} = "
                         f"{price * count:.2f} руб.")
        return "\n".join(lines)


def task_19():
    """Задание 19*: успешные добавления и все виды ошибок."""
    warehouse = Inventory()
    warehouse.add_item("Клавиатура", 1500, 10)
    warehouse.add_item("Мышь", 800.50, 25)
    warehouse.add_item("Монитор", 12000, 4)
    warehouse.add_item("Клавиатура беспроводная", 2500, 6)

    print(warehouse)
    print(f"\nИтоговая стоимость: {warehouse.total_value:.2f} руб.")

    print("\nПоиск по подстроке 'клавиатура':")
    for name, (price, count) in warehouse.search("КЛАВИАТУРА").items():
        print(f"  {name}: {price:.2f} руб. x {count}")

    errors = [
        ("неверный тип названия", 123, 100, 5),
        ("неверный тип цены", "Монитор", "12000", 4),
        ("неверный тип количества", "Монитор", 12000, 4.5),
        ("цена не больше нуля", "Монитор", 0, 4),
        ("отрицательное количество", "Монитор", 12000, -1),
    ]
    print()
    for description, name, price, count in errors:
        try:
            warehouse.add_item(name, price, count)
        except (TypeError, ValueError) as error:
            print(f"{description}: {type(error).__name__}: {error}")


# ======================================================================
# ЗАДАНИЕ 20*. Класс Registry: реестр всех созданных экземпляров
# ======================================================================


class Registry:
    """Реестр всех созданных экземпляров класса.

    В реестре хранятся слабые ссылки (weakref), а не сами объекты.
    Сильная ссылка в списке класса удерживала бы каждый объект живым,
    поэтому метод __del__ не вызывался бы никогда, пока существует
    реестр, и список не уменьшался бы.
    """

    __registry = []

    def __init__(self, name):
        self.name = name
        Registry.__registry.append(weakref.ref(self))

    def __del__(self):
        for link in Registry.__registry:
            if link() is self:
                Registry.__registry.remove(link)
                print(f"Объект «{self.name}» удалён из реестра")
                break

    @classmethod
    def all_instances(cls):
        """Вернуть список всех живых экземпляров."""
        return [link() for link in cls.__registry if link() is not None]

    @classmethod
    def count(cls):
        """Вернуть количество живых экземпляров."""
        return len([link for link in cls.__registry if link() is not None])


def task_20():
    """Задание 20*: реестр объектов, рост и уменьшение списка."""
    print("До создания экземпляров Registry.count() =", Registry.count())

    r1 = Registry("объект-1")
    r2 = Registry("объект-2")
    r3 = Registry("объект-3")
    r4 = Registry("объект-4")
    r5 = Registry("объект-5")

    print("Registry.count() =", Registry.count())
    print("Реестр:")
    for obj in Registry.all_instances():
        print(" ", obj.name)

    print("\nУдаляем объект-2 и объект-4")
    del r2, r4

    print("Registry.count() =", Registry.count())
    print("Реестр:")
    for obj in Registry.all_instances():
        print(" ", obj.name)

    print("\nМетод класса вызывается без создания экземпляра:",
          Registry.count())

    # Переменная цикла obj тоже является ссылкой на последний объект,
    # поэтому перед удалением её нужно освободить.
    obj = None

    print("\nУдаляем оставшиеся объекты")
    del r1, r3, r5
    print("Registry.count() =", Registry.count())

    # Вывод: __registry объявлен на уровне класса, поэтому список один на
    # весь класс, а не на каждый объект: его видят все экземпляры, методы
    # класса и __del__. Приватное имя внутри класса автоматически
    # превращается в _Registry__registry, а @classmethod даёт доступ к
    # этому атрибуту через cls без создания объекта.


# ======================================================================
# Запуск заданий
# ======================================================================

TASKS = {
    1: ("Класс Point (точка на плоскости)", task_01),
    2: ("Класс Person с проверкой возраста", task_02),
    3: ("Класс Car и работа с атрибутами объекта", task_03),
    4: ("Класс Student со списком оценок", task_04),
    5: ("Пустой класс как именованный контейнер", task_05),
    6: ("Класс Circle с вычисляемыми методами", task_06),
    7: ("Класс Rectangle и поиск максимума по площади", task_07),
    8: ("Атрибут класса — счётчик точек", task_08),
    9: ("Счётчик живых экземпляров и метод __del__", task_09),
    10: ("Класс Temperature: __str__ и __repr__", task_10),
    11: ("Temperature 2.0: приватное значение и свойство fahrenheit",
         task_11),
    12: ("Класс Wallet: свойство с валидацией", task_12),
    13: ("Класс BankAccount с историей операций", task_13),
    14: ("Класс Book с приватным флагом доступности", task_14),
    15: ("Класс Employee: приватная зарплата и повышение", task_15),
    16: ("Ведомость по банковским счетам", task_16),
    17: ("Рейтинг студентов", task_17),
    18: ("Класс Library — контейнер книг", task_18),
    19: ("Класс Inventory: строгая валидация состояния", task_19),
    20: ("Класс Registry: реестр всех созданных экземпляров", task_20),
}


def run_task(number):
    """Выполнить одно задание по его номеру."""
    title, function = TASKS[number]
    print()
    print("=" * 78)
    print(f"ЗАДАНИЕ {number}. {title}")
    print("=" * 78)
    function()


def main():
    """Выполнить все задания или одно задание, указанное в аргументе."""
    if len(sys.argv) > 1:
        try:
            number = int(sys.argv[1])
            run_task(number)
        except (ValueError, KeyError):
            print("Укажите номер задания от 1 до 20, например: "
                  "python main.py 5")
        return

    print("ПРАКТИЧЕСКАЯ РАБОТА № 2")
    print("Объявление класса, создание экземпляров класса")
    for number in TASKS:
        run_task(number)
    print()
    print("=" * 78)
    print("Все задания 1–20 выполнены.")
    print("=" * 78)


if __name__ == "__main__":
    main()
