import math

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


a = Point(0, 0)
b = Point(3, 4)

print(a)