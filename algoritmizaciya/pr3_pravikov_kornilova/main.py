"""
Практическая работа № 3.

Тема: «Наследование. Создание производного класса. Переопределение методов.
Вызов методов базового класса (super())».

Группа: 14-434.
Обучающиеся: Правиков Д. В., Корнилова Л. Д.
Дата выполнения: 06.11.2026.

Программа последовательно выполняет задания 1-20. Каждое задание отделено
комментарием и запускается своей функцией task_XX().
"""

import math


# ============================================================================
# ЗАДАНИЕ 1. Иерархия животных
# ============================================================================

class Animal:
    """Базовый класс животного."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        """Возвращает звук, который издаёт животное."""
        return "Какой-то звук"

    def info(self):
        """Возвращает строку вида «Рекс: Гав!»."""
        return f"{self.name}: {self.speak()}"


class Dog(Animal):
    """Производный класс собаки: добавляет породу и переопределяет speak()."""

    def __init__(self, name, breed="не указана"):
        super().__init__(name)              # инициализация базовой части
        self.breed = breed                  # собственный атрибут

    def speak(self):
        return "Гав!"


class Cat(Animal):
    """Производный класс кошки: переопределяет speak()."""

    def speak(self):
        return "Мяу!"


class Cow(Animal):
    """Производный класс коровы: переопределяет speak()."""

    def speak(self):
        return "Му!"


def task_01():
    """Задание 1. Полиморфный вывод и проверка иерархии."""
    print("\n" + "=" * 70)
    print("Задание 1. Иерархия животных")
    print("=" * 70)

    # Dog добавил атрибут breed и свою версию speak();
    # Cat и Cow добавили только собственную версию speak().
    zoo = [Dog("Рекс", "овчарка"), Cat("Мурка"), Cow("Зорька")]
    for animal in zoo:
        print(animal.info())

    print("isinstance(zoo[0], Animal):", isinstance(zoo[0], Animal))
    print("issubclass(Dog, Animal):", issubclass(Dog, Animal))


# ============================================================================
# ЗАДАНИЕ 2. Person -> Student: расширение метода
# ============================================================================

class Person:
    """Базовый класс человека."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Возвращает строку вида «Я Анна, мне 19 лет.»."""
        return f"Я {self.name}, мне {self.age} лет."


class Student(Person):
    """Студент: добавляет группу и дополняет introduce() через super()."""

    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group

    def introduce(self):
        # Не заменяем поведение базового класса, а дополняем его.
        return super().introduce() + f" Учусь в группе {self.group}."


def task_02():
    """Задание 2. Переопределение introduce() с вызовом super()."""
    print("\n" + "=" * 70)
    print("Задание 2. Person -> Student: расширение метода")
    print("=" * 70)

    person = Person("Анна", 19)
    student = Student("Анна", 19, "14-434")

    print("person.introduce(): ", person.introduce())
    print("student.introduce():", student.introduce())
    print("isinstance(person, Person): ", isinstance(person, Person))
    print("isinstance(student, Person):", isinstance(student, Person))

    # Строка студента содержит базовую часть и дополнение о группе:
    # поведение Person не потеряно, а расширено вызовом super().introduce().


# ============================================================================
# ЗАДАНИЕ 3. Проверка иерархии: issubclass, isinstance и __bases__
# ============================================================================

def task_03():
    """Задание 3. Проверки наследования и атрибут __bases__."""
    print("\n" + "=" * 70)
    print("Задание 3. Проверка иерархии: issubclass, isinstance и __bases__")
    print("=" * 70)

    student = Student("Анна", 19, "14-434")

    print("issubclass(Dog, Animal):    ", issubclass(Dog, Animal))
    print("issubclass(Student, Person):", issubclass(Student, Person))
    print("issubclass(Person, Dog):    ", issubclass(Person, Dog))
    print("isinstance(student, Person):", isinstance(student, Person))
    print('isinstance("текст", Person):', isinstance("текст", Person))

    print("Dog.__bases__:    ", Dog.__bases__)
    print("Student.__bases__:", Student.__bases__)
    print("Person.__bases__: ", Person.__bases__)

    # У класса Person в скобках не указан базовый класс, поэтому Python
    # неявно наследует его от object — общего корня всей иерархии классов.
    # Именно поэтому Person.__bases__ равен (object,), а не пустому кортежу.


# ============================================================================
# ЗАДАНИЕ 4. Employee -> Manager: наследование без переопределений
# ============================================================================

def task_04():
    """Задание 4. Унаследованный метод info() работает без изменений."""
    print("\n" + "=" * 70)
    print("Задание 4. Employee -> Manager: наследование без переопределений")
    print("=" * 70)

    class Employee:
        """Сотрудник с именем и окладом."""

        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def info(self):
            return f"{self.name}: оклад {self.salary}"

    class Manager(Employee):
        """Менеджер: добавляет отдел, но использует унаследованный info()."""

        def __init__(self, name, salary, department):
            super().__init__(name, salary)
            self.department = department

    manager = Manager("Анна", 80000, "отдел разработки")

    # info() не переопределён: Manager получил весь интерфейс Employee.
    print(manager.info())
    print("name:      ", manager.name)
    print("salary:    ", manager.salary)
    print("department:", manager.department)


# ============================================================================
# ЗАДАНИЕ 5. Что именно наследуется — эксперимент
# ============================================================================

def task_05():
    """Задание 5. hasattr() для унаследованных и собственных имён."""
    print("\n" + "=" * 70)
    print("Задание 5. Что именно наследуется — эксперимент")
    print("=" * 70)

    class Device:
        """Устройство: vendor — атрибут класса, общий для наследников."""

        vendor = "Lenovo"

        def turn_on(self):
            return f"{self.vendor}: устройство включено"

    class Laptop(Device):
        """Ноутбук: добавляет собственный метод compile()."""

        def compile(self):
            return "Компиляция программы завершена"

    laptop = Laptop()

    for attribute in ("turn_on", "compile", "vendor"):
        print(f"hasattr(laptop, '{attribute}'):", hasattr(laptop, attribute))

    print("isinstance(laptop, object):", isinstance(laptop, object))
    print("Device.turn_on(laptop):    ", Device.turn_on(laptop))

    # turn_on и vendor унаследованы от Device, compile объявлен в Laptop.
    # Вызов Device.turn_on(laptop) работает, потому что laptop — наследник
    # Device: объект-наследник допустим там, где ожидается объект базового
    # класса. Поиск атрибута идёт по цепочке Laptop -> Device -> object.


# ============================================================================
# ЗАДАНИЕ 6. Расчётная иерархия сотрудников
# ============================================================================

class Employee:
    """Базовый класс сотрудника: оклад и строка о доходе."""

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def income(self):
        return self.salary

    def info(self):
        return f"{self.name}: доход {self.income():.0f} руб."


class Manager(Employee):
    """Руководитель: оклад плюс бонус."""

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def income(self):
        return super().income() + self.bonus


class Developer(Employee):
    """Разработчик: надбавка за уровень."""

    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self.level = level

    def income(self):
        coefficient = {1: 1.0, 2: 1.2, 3: 1.5}.get(self.level, 1.0)
        return self.salary * coefficient


class Intern(Employee):
    """Стажёр: почасовая оплата."""

    def __init__(self, name, hourly_rate, hours):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def income(self):
        return self.hourly_rate * self.hours


def task_06():
    """Задание 6. Четыре типа сотрудников и суммарный доход."""
    print("\n" + "=" * 70)
    print("Задание 6. Расчётная иерархия сотрудников")
    print("=" * 70)

    staff = [
        Employee("Галина", 60000),
        Manager("Анна", 80000, 15000),
        Developer("Борис", 70000, 3),
        Intern("Виктор", 500, 80),
    ]

    for employee in staff:
        print(employee.info())

    total = sum(employee.income() for employee in staff)
    print(f"Суммарный доход: {total:.0f} руб.")


# ============================================================================
# ЗАДАНИЕ 7. Разбор ошибки: пропущенный super().__init__
# ============================================================================

def task_07():
    """Задание 7. AttributeError при пропуске super().__init__()."""
    print("\n" + "=" * 70)
    print("Задание 7. Разбор ошибки: пропущенный super().__init__")
    print("=" * 70)

    class Product:
        """Товар с названием и ценой."""

        def __init__(self, name, price):
            self.name = name
            self.price = price

    class DiscountedProductBroken(Product):
        """Первая, ошибочная версия: super().__init__() не вызывается."""

        def __init__(self, name, price, discount):
            # ОШИБКА: базовая часть не инициализирована.
            self.discount = discount
            # Атрибуты name и price не созданы.

    class DiscountedProduct(Product):
        """Исправленная версия: сначала инициализируется базовая часть."""

        def __init__(self, name, price, discount):
            super().__init__(name, price)   # первая строка — правило
            self.discount = discount

        def final_price(self):
            return self.price * (1 - self.discount)

    broken = DiscountedProductBroken("Ноутбук", 50000, 0.1)
    try:
        print("Имя ошибочного объекта:", broken.name)
    except AttributeError as error:
        print("Перехвачено AttributeError:", error)
        print("Причина: в DiscountedProductBroken не вызван")
        print("super().__init__(name, price), поэтому атрибуты name и price")
        print("не были созданы.")

    fixed = DiscountedProduct("Ноутбук", 50000, 0.1)
    print("Исправленный объект:", fixed.name, fixed.price, fixed.discount)
    print(f"Цена со скидкой: {fixed.final_price():.0f} руб.")

    # Правило: в переопределённом __init__ вызов super().__init__(...)
    # выполняется первой строкой, чтобы базовая часть была готова.


# ============================================================================
# ЗАДАНИЕ 8. Транспорт: Vehicle -> Car, Bicycle
# ============================================================================

def task_08():
    """Задание 8. Дополнение describe() в наследниках."""
    print("\n" + "=" * 70)
    print("Задание 8. Транспорт: Vehicle -> Car, Bicycle")
    print("=" * 70)

    class Vehicle:
        """Транспортное средство с маркой и моделью."""

        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def describe(self):
            return f"Транспорт: {self.brand} {self.model}"

    class Car(Vehicle):
        """Автомобиль: добавляет число дверей."""

        def __init__(self, brand, model, doors):
            super().__init__(brand, model)
            self.doors = doors

        def describe(self):
            return super().describe() + f", дверей: {self.doors}"

    class Bicycle(Vehicle):
        """Велосипед: добавляет тип рамы."""

        def __init__(self, brand, model, frame_type):
            super().__init__(brand, model)
            self.frame_type = frame_type

        def describe(self):
            return super().describe() + f", тип рамы: {self.frame_type}"

    vehicles = [
        Car("Lada", "Vesta", 4),
        Bicycle("Stels", "Navigator", "горная"),
        Car("Kia", "Rio", 4),
        Bicycle("Forward", "Sport", "шоссейная"),
    ]

    for vehicle in vehicles:
        print(vehicle.describe())


# ============================================================================
# ЗАДАНИЕ 9. Точка на плоскости -> точка в пространстве
# ============================================================================

def task_09():
    """Задание 9. Расстояние в 2D и 3D, переопределение __str__."""
    print("\n" + "=" * 70)
    print("Задание 9. Точка на плоскости -> точка в пространстве")
    print("=" * 70)

    class Point2D:
        """Точка на плоскости."""

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance_to(self, other):
            return math.hypot(self.x - other.x, self.y - other.y)

        def __str__(self):
            return f"Point ({self.x}; {self.y})"

    class Point3D(Point2D):
        """Точка в пространстве: добавляет координату z."""

        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z = z

        def distance_to(self, other):
            return math.hypot(
                self.x - other.x,
                self.y - other.y,
                self.z - other.z,
            )

        def __str__(self):
            # Берём базовую строку и добавляем координату z.
            return super().__str__()[:-1] + f"; {self.z})"

    p1 = Point2D(2, 3)
    p2 = Point2D(5, 7)
    print(p1, "->", p2)
    print("Расстояние в 2D:", p1.distance_to(p2))

    p3 = Point3D(1, 2, 3)
    p4 = Point3D(4, 6, 3)
    print(p3, "->", p4)
    print("Расстояние в 3D:", p3.distance_to(p4))

    # Переопределение заменяет метод, а super() позволяет дополнить
    # базовую реализацию, не копируя её.


# ============================================================================
# ЗАДАНИЕ 10. Rectangle -> Square: преобразование аргументов
# ============================================================================

def task_10():
    """Задание 10. Квадрат переиспользует методы прямоугольника."""
    print("\n" + "=" * 70)
    print("Задание 10. Rectangle -> Square: преобразование аргументов")
    print("=" * 70)

    class Rectangle:
        """Прямоугольник с шириной и высотой."""

        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

    class Square(Rectangle):
        """Квадрат — частный случай прямоугольника."""

        def __init__(self, side):
            # Квадрат передаёт в базовый инициализатор две равные стороны.
            super().__init__(side, side)

    square = Square(5)

    print("Площадь квадрата:  ", square.area())
    print("Периметр квадрата: ", square.perimeter())
    print("isinstance(square, Rectangle):", isinstance(square, Rectangle))

    # Квадрат является прямоугольником (is-a), поэтому наследование уместно.
    # super().__init__(side, side) позволил не писать формулы площади и
    # периметра заново: они унаследованы от Rectangle.


# ============================================================================
# ЗАДАНИЕ 11. Фигуры: Shape -> Rectangle, Circle
# ============================================================================

class Shape:
    """Базовый класс фигуры."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Площадь базовой фигуры по умолчанию равна нулю."""
        return 0.0

    def __str__(self):
        return f"{self.name}: площадь {self.area():.2f}"


class Rectangle(Shape):
    """Прямоугольник: площадь равна произведению сторон."""

    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    """Круг: площадь равна pi * r^2."""

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def task_11():
    """Задание 11. Сортировка фигур по возрастанию площади."""
    print("\n" + "=" * 70)
    print("Задание 11. Фигуры: Shape -> Rectangle, Circle")
    print("=" * 70)

    figures = [
        Rectangle("Прямоугольник A", 4, 5),
        Circle("Круг B", 2),
        Rectangle("Прямоугольник C", 3, 3),
        Circle("Круг D", 1.5),
    ]

    print("area() базового Shape:", Shape("Базовая фигура").area())
    print("Фигуры по возрастанию площади:")
    for figure in sorted(figures, key=lambda f: f.area()):
        print(" ", figure)

    # key=lambda f: f.area() работает без проверки типов: у каждой фигуры
    # есть метод area(), а нужную версию выбирает динамическая диспетчеризация.


# ============================================================================
# ЗАДАНИЕ 12. Диспетчеризация: функция работает с базовым классом
# ============================================================================

def task_12():
    """Задание 12. broadcast() и новый класс без изменения функции."""
    print("\n" + "=" * 70)
    print("Задание 12. Диспетчеризация: функция работает с базовым классом")
    print("=" * 70)

    class Notification:
        """Базовое уведомление."""

        def send(self):
            return "Базовое уведомление отправлено"

    class EmailNotification(Notification):
        """Уведомление по электронной почте."""

        def __init__(self, address):
            self.address = address

        def send(self):
            return f"Email на {self.address}: сообщение отправлено"

    class SmsNotification(Notification):
        """Уведомление по SMS."""

        def __init__(self, phone):
            self.phone = phone

        def send(self):
            return f"SMS на {self.phone}: сообщение отправлено"

    def broadcast(messages):
        """Печатает результат send() для каждого уведомления."""
        for notification in messages:
            print(notification.send())

    print("Первый набор уведомлений:")
    broadcast([
        EmailNotification("student@example.ru"),
        SmsNotification("+7 (900) 123-45-67"),
        Notification(),
    ])

    class PushNotification(Notification):
        """Push-уведомление, добавленное после написания broadcast()."""

        def __init__(self, device):
            self.device = device

        def send(self):
            return f"Push на устройство {self.device}: сообщение отправлено"

    print("После добавления PushNotification:")
    # Функция broadcast() не изменилась, но работает с новым классом.
    broadcast([
        EmailNotification("student@example.ru"),
        SmsNotification("+7 (900) 123-45-67"),
        PushNotification("Pixel"),
    ])

    # Это динамическая диспетчеризация: broadcast() вызывает n.send(),
    # и Python сам выбирает реализацию send() по фактическому классу объекта.


# ============================================================================
# ЗАДАНИЕ 13. Два способа вызвать базовый метод
# ============================================================================

def task_13():
    """Задание 13. super().hello() и Greeter.hello(self)."""
    print("\n" + "=" * 70)
    print("Задание 13. Два способа вызвать базовый метод")
    print("=" * 70)

    class Greeter:
        """Простое приветствие."""

        def hello(self):
            return "Привет!"

    class FormalGreeter(Greeter):
        """Официальное приветствие, дополняющее базовое."""

        def hello(self):
            return super().hello() + " Добрый день!"

        def hello_direct(self):
            return Greeter.hello(self) + " Добрый день!"

    greeter = FormalGreeter()
    first = greeter.hello()
    second = greeter.hello_direct()

    print("Через super().hello():     ", first)
    print("Через Greeter.hello(self): ", second)
    print("Результаты совпадают:      ", first == second)

    # super() предпочтительнее: он автоматически идёт по MRO и продолжит
    # работать, если между FormalGreeter и Greeter появится новый класс.
    # Прямой вызов Greeter.hello(self) жёстко привязан к имени класса.


# ============================================================================
# ЗАДАНИЕ 14. Приватное состояние и наследование
# ============================================================================

def task_14():
    """Задание 14. Name mangling и работа через интерфейс базового класса."""
    print("\n" + "=" * 70)
    print("Задание 14. Приватное состояние и наследование")
    print("=" * 70)

    class Account:
        """Счёт с приватным балансом и проверками операций."""

        def __init__(self, owner, balance=0.0):
            if balance < 0:
                raise ValueError("Начальный баланс не может быть отрицательным")
            self.owner = owner
            self.__balance = float(balance)

        @property
        def balance(self):
            """Баланс доступен только для чтения."""
            return self.__balance

        def deposit(self, amount):
            if amount <= 0:
                raise ValueError("Сумма должна быть положительной")
            self.__balance += amount

        def withdraw(self, amount):
            if amount <= 0:
                raise ValueError("Сумма должна быть положительной")
            if amount > self.__balance:
                raise ValueError("Недостаточно средств")
            self.__balance -= amount

        def __str__(self):
            return f"Счёт ({self.owner}): {self.__balance:.2f} руб."

    class CreditAccount(Account):
        """Кредитный счёт: добавляет лимит и доступную сумму."""

        def __init__(self, owner, balance=0.0, limit=0.0):
            super().__init__(owner, balance)
            if limit < 0:
                raise ValueError("Лимит не может быть отрицательным")
            self.limit = limit

        def available(self):
            return self.balance + self.limit

        def check_private_access(self):
            """Показывает, что __balance базового класса недоступен напрямую."""
            try:
                return self.__balance
            except AttributeError as error:
                return f"AttributeError: {error}"

    account = CreditAccount("Иванов И. И.", 1000, 500)

    print("Начальное состояние:", account)
    account.deposit(500)
    print("После пополнения на 500:", account)
    account.withdraw(300)
    print("После снятия 300:      ", account)
    print("Доступная сумма (баланс + лимит):", account.available())

    print("Прямое обращение к __balance из CreditAccount:")
    print(" ", account.check_private_access())
    print("Причина: name mangling превращает self.__balance в")
    print("_CreditAccount__balance, а реальный атрибут называется")
    print("_Account__balance. Наследник должен работать через свойство")
    print("balance и методы deposit()/withdraw().")

    try:
        account.withdraw(10000)
    except ValueError as error:
        print("Перехвачено ValueError:", error)


# ============================================================================
# ЗАДАНИЕ 15. Многоуровневая иерархия: Person -> Employee -> Manager
# ============================================================================

def task_15():
    """Задание 15. Три уровня наследования и MRO."""
    print("\n" + "=" * 70)
    print("Задание 15. Многоуровневая иерархия: Person -> Employee -> Manager")
    print("=" * 70)

    class Person:
        """Человек."""

        def __init__(self, name):
            self.name = name

        def introduce(self):
            return f"Я {self.name}"

    class Employee(Person):
        """Сотрудник: дополняет представление сведениями о зарплате."""

        def __init__(self, name, salary):
            super().__init__(name)
            self.salary = salary

        def introduce(self):
            return super().introduce() + f", работаю и получаю {self.salary} руб."

    class Manager(Employee):
        """Менеджер: дополнительно сообщает об отделе."""

        def __init__(self, name, salary, department):
            super().__init__(name, salary)
            self.department = department

        def introduce(self):
            return super().introduce() + f", руковожу отделом {self.department}"

    person = Person("Анна")
    employee = Employee("Борис", 70000)
    manager = Manager("Вера", 90000, "разработки")

    print("Person:  ", person.introduce())
    print("Employee:", employee.introduce())
    print("Manager: ", manager.introduce())

    print("Manager.__mro__:", Manager.__mro__)
    print("isinstance(manager, Person):", isinstance(manager, Person))
    print("issubclass(Manager, Person):", issubclass(Manager, Person))


# ============================================================================
# ЗАДАНИЕ 16. Ведомость доходов
# ============================================================================

def task_16():
    """Задание 16. Агрегатные операции по смешанному списку."""
    print("\n" + "=" * 70)
    print("Задание 16. Ведомость доходов")
    print("=" * 70)

    staff = [
        Employee("Галина", 60000),
        Manager("Анна", 80000, 15000),
        Developer("Борис", 70000, 3),
        Intern("Виктор", 500, 80),
        Manager("Дмитрий", 90000, 20000),
        Developer("Елена", 65000, 2),
        Intern("Олег", 450, 100),
    ]

    print("Ведомость:")
    for employee in staff:
        print(" ", employee.info())

    total_fund = sum(employee.income() for employee in staff)
    average = total_fund / len(staff)
    best = max(staff, key=lambda e: e.income())
    above_average = [e for e in staff if e.income() > average]

    print(f"Суммарный фонд оплаты труда: {total_fund:.0f} руб.")
    print(f"Средний доход: {average:.2f} руб.")
    print("Сотрудник с максимальным доходом:", best.info())
    print("Сотрудники с доходом выше среднего:")
    for employee in above_average:
        print(" ", employee.info())
    print("Количество таких сотрудников:", len(above_average))

    # В коде обработки нет isinstance: sum, max и списочное включение
    # работают с общим интерфейсом income()/info(). Разные реализации
    # выбираются динамически, поэтому смешанный список обрабатывается едино.


# ============================================================================
# ЗАДАНИЕ 17. Фигуры: сортировка, агрегаты и подсчёт по типам
# ============================================================================

def task_17():
    """Задание 17. Сортировка, сумма, max и подсчёт по isinstance."""
    print("\n" + "=" * 70)
    print("Задание 17. Фигуры: сортировка, агрегаты и подсчёт по типам")
    print("=" * 70)

    figures = [
        Rectangle("Прямоугольник 1", 4, 5),
        Circle("Круг 1", 2),
        Rectangle("Прямоугольник 2", 3, 7),
        Circle("Круг 2", 3),
        Rectangle("Прямоугольник 3", 6, 2),
        Circle("Круг 3", 1),
        Rectangle("Прямоугольник 4", 5, 5),
    ]

    print("Фигуры по убыванию площади:")
    for figure in sorted(figures, key=lambda f: f.area(), reverse=True):
        print(" ", figure)

    total_area = sum(figure.area() for figure in figures)
    largest = max(figures, key=lambda f: f.area())

    print(f"Суммарная площадь: {total_area:.2f}")
    print("Самая большая фигура:", largest)

    circles = [figure for figure in figures if isinstance(figure, Circle)]
    rectangles = [
        figure for figure in figures if isinstance(figure, Rectangle)
    ]
    print("Количество кругов:", len(circles))
    print("Количество прямоугольников:", len(rectangles))

    # Все фигуры имеют единый интерфейс area(), поэтому sorted, sum и max
    # работают без проверки типов; isinstance нужен только для подсчёта.


# ============================================================================
# ЗАДАНИЕ 18. Библиотека: иерархия материалов и класс-контейнер
# ============================================================================

def task_18():
    """Задание 18. Композиция, полиморфный вывод и проверка типа."""
    print("\n" + "=" * 70)
    print("Задание 18. Библиотека: иерархия материалов и класс-контейнер")
    print("=" * 70)

    class LibraryItem:
        """Материал библиотеки: общие название и год."""

        def __init__(self, title, year):
            self.title = title
            self.year = year

        def describe(self):
            return f"{self.title} ({self.year})"

    class Book(LibraryItem):
        """Книга: добавляет автора и число страниц."""

        def __init__(self, title, year, author, pages):
            super().__init__(title, year)
            self.author = author
            self.pages = pages

        def describe(self):
            return (
                super().describe()
                + f", автор: {self.author}, страниц: {self.pages}"
            )

    class Magazine(LibraryItem):
        """Журнал: добавляет номер выпуска и месяц."""

        def __init__(self, title, year, issue, month):
            super().__init__(title, year)
            self.issue = issue
            self.month = month

        def describe(self):
            return (
                super().describe()
                + f", выпуск: {self.issue}, месяц: {self.month}"
            )

    class Library:
        """Библиотека хранит материалы в приватном списке __items."""

        def __init__(self):
            self.__items = []

        def add_item(self, item):
            if not isinstance(item, LibraryItem):
                raise TypeError(
                    "В библиотеку можно добавлять только LibraryItem"
                )
            self.__items.append(item)

        def show_all(self):
            for item in self.__items:
                print(" ", item.describe())

        def count_by_class(self, cls):
            return sum(1 for item in self.__items if isinstance(item, cls))

    library = Library()
    library.add_item(Book("Война и мир", 1873, "Л. Н. Толстой", 1300))
    library.add_item(Book("Преступление и наказание", 1866, "Ф. М. Достоевский", 480))
    library.add_item(Book("Мастер и Маргарита", 1967, "М. А. Булгаков", 480))
    library.add_item(Magazine("Наука и жизнь", 2024, 1, "январь"))
    library.add_item(Magazine("Знание — сила", 2024, 2, "февраль"))

    print("Все материалы библиотеки:")
    library.show_all()
    print("Количество книг:", library.count_by_class(Book))
    print("Количество журналов:", library.count_by_class(Magazine))

    try:
        library.add_item("Это строка, а не материал библиотеки")
    except TypeError as error:
        print("Перехвачено TypeError:", error)

    try:
        print(library.__items)
    except AttributeError as error:
        print("Перехвачено AttributeError:", error)
        print("Список __items приватный: снаружи доступен только через")
        print("add_item(), show_all() и count_by_class().")

    # Library — композиция: библиотека имеет материалы (has-a), а не
    # является материалом. Поэтому Library не наследует LibraryItem.


# ============================================================================
# ЗАДАНИЕ 19*. Трёхуровневая иерархия счетов
# ============================================================================

def task_19():
    """Задание 19. Смешанный список счетов и начисление процентов."""
    print("\n" + "=" * 70)
    print("Задание 19*. Трёхуровневая иерархия счетов")
    print("=" * 70)

    class Account:
        """Базовый счёт с приватным балансом."""

        def __init__(self, owner, balance=0.0):
            if balance < 0:
                raise ValueError("Начальный баланс не может быть отрицательным")
            self.owner = owner
            self.__balance = float(balance)

        @property
        def balance(self):
            return self.__balance

        def deposit(self, amount):
            if amount <= 0:
                raise ValueError("Сумма должна быть положительной")
            self.__balance += amount

        def withdraw(self, amount):
            if amount <= 0:
                raise ValueError("Сумма должна быть положительной")
            if amount > self.__balance:
                raise ValueError("Недостаточно средств")
            self.__balance -= amount

        def __str__(self):
            return f"Счёт ({self.owner}): {self.__balance:.2f} руб."

    class SavingsAccount(Account):
        """Накопительный счёт с приватной ставкой."""

        def __init__(self, owner, balance=0.0, rate=0.05):
            super().__init__(owner, balance)
            if rate <= 0:
                raise ValueError("Ставка должна быть положительной")
            self.__rate = rate

        @property
        def rate(self):
            return self.__rate

        def add_interest(self):
            interest = self.balance * self.__rate
            self.deposit(interest)
            return interest

        def __str__(self):
            return super().__str__() + f" | ставка {self.__rate:.0%}"

    class VipSavingsAccount(SavingsAccount):
        """VIP-счёт: повышенная ставка и бонус за лояльность."""

        def __init__(self, owner, balance=0.0, rate=0.1):
            super().__init__(owner, balance, rate)

        def add_loyalty_bonus(self, amount=1000.0):
            self.deposit(amount)

        def __str__(self):
            return super().__str__() + " | VIP"

    accounts = [
        Account("Петров П. П.", 5000),
        SavingsAccount("Сидоров С. С.", 10000, 0.05),
        VipSavingsAccount("Кузнецов К. К.", 20000),
        SavingsAccount("Смирнова А. А.", 15000, 0.07),
    ]

    # Проценты начисляем только накопительным счетам; VIP-счёт тоже является
    # SavingsAccount, поэтому проценты получает, а затем ещё и бонус.
    for account in accounts:
        if isinstance(account, SavingsAccount):
            account.add_interest()
        if isinstance(account, VipSavingsAccount):
            account.add_loyalty_bonus()

    print("Состояние счетов после начисления:")
    for account in accounts:
        print(" ", account)

    try:
        SavingsAccount("Ошибочный счёт", 1000, -0.05)
    except ValueError as error:
        print("Перехвачено ValueError:", error)

    # Каждый уровень добавляет только своё: Account хранит баланс и проверки,
    # SavingsAccount — ставку и проценты, VipSavingsAccount — бонус и метку.
    # Строки __str__ последовательно дополняются через super().


# ============================================================================
# ЗАДАНИЕ 20*. Фабрика объектов и группировка по типам
# ============================================================================

def task_20():
    """Задание 20. Создание объектов через словарь-фабрику без if."""
    print("\n" + "=" * 70)
    print("Задание 20*. Фабрика объектов и группировка по типам")
    print("=" * 70)

    factory = {"dog": Dog, "cat": Cat, "cow": Cow}

    specs = [
        ("dog", "Рекс", "овчарка"),
        ("cat", "Мурка"),
        ("cow", "Зорька"),
    ]

    animals = []
    for spec in specs:
        code, args = spec[0], spec[1:]
        # Класс извлекается из словаря и вызывается как обычная функция.
        animals.append(factory[code](*args))

    print("Животные, созданные фабрикой:")
    for animal in animals:
        print(" ", animal.info())

    counts = {
        cls.__name__: sum(1 for animal in animals if isinstance(animal, cls))
        for cls in (Dog, Cat, Cow)
    }
    print("Количество по типам:", counts)

    # Классы в Python — объекты первого класса: их можно хранить в словаре,
    # передавать в функции и вызывать. Чтобы добавить новый вид животного,
    # достаточно добавить одну строку в factory и класс-наследник Animal;
    # цикл создания объектов и подсчёта останется без изменений.


# ============================================================================
# ЗАПУСК ВСЕХ ЗАДАНИЙ
# ============================================================================

def main():
    """Последовательно выполняет задания 1-20."""
    tasks = [
        task_01,
        task_02,
        task_03,
        task_04,
        task_05,
        task_06,
        task_07,
        task_08,
        task_09,
        task_10,
        task_11,
        task_12,
        task_13,
        task_14,
        task_15,
        task_16,
        task_17,
        task_18,
        task_19,
        task_20,
    ]

    for task in tasks:
        task()


if __name__ == "__main__":
    main()
