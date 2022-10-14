from math import sqrt, acos
import math


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False

    # Векторное произведение
    @staticmethod
    def vect(a, b, c, d):
        return (b.x - a.x) * (d.y - c.y) - (b.y - a.y) * (d.x - c.x)

    # Угол между векторами (a, b) и (с, d)
    @staticmethod
    def angle(a, b, c, d):
        t = ((b.x - a.x) * (d.x - c.x) + (d.y - c.y)
             * (b.y - a.y)) / (a.dist(b)*(c.dist(d)))
        if t < 0:
            return 180.0 - math.degrees(math.acos(t))
        else:
            return math.degrees(math.acos(t))

    # Пересекаются ли два отрезка?
    @staticmethod
    def crossing(a, b, c, d):
        if (R2Point.vect(c, d, c, a) * R2Point.vect(c, d, c, b) <= 0) \
             and (R2Point.vect(a, b, a, c) * R2Point.vect(a, b, a, d) <= 0):
            return R2Point.angle(a, b, c, d)
        else:
            return 0


if __name__ == "__main__":
    print(math.acos(-0.5547001962252291))
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
    print(R2Point.area(a, c, b))
