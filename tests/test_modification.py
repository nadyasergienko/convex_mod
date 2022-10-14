from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.t = Void()

    def test00(self):
        Figure.fixed_first_point = R2Point(-1.0, 2.0)
        Figure.fixed_last_point = R2Point(1.0, 0.0)
        self.t = self.t.add(R2Point(-1.0, 0.0))
        assert self.t.s() is None

    def test0(self):
        Figure.fixed_first_point = R2Point(0.0, 0.5)
        Figure.fixed_last_point = R2Point(0.0, 3.0)
        self.t = self.t.add(R2Point(0.0, 0.0))
        self.t = self.t.add(R2Point(2.0, 2.0))
        self.t = self.t.add(R2Point(0.0, 4.0))
        self.t = self.t.add(R2Point(-2.0, 2.0))
        assert self.t.s() == 0.0

    def test1(self):
        Figure.fixed_first_point = R2Point(3.0, 3.0)
        Figure.fixed_last_point = R2Point(0.0, 0.0)
        self.t = self.t.add(R2Point(4.0, 2.0))
        self.t = self.t.add(R2Point(0.0, 2.0))
        assert self.t.s() == 90.0

    def test2(self):
        Figure.fixed_first_point = R2Point(0.0, 4.0)
        Figure.fixed_last_point = R2Point(0.0, 0.0)
        self.t = self.t.add(R2Point(2.0, 2.0))
        self.t = self.t.add(R2Point(-2.0, 2.0))
        self.t = self.t.add(R2Point(0.0, 4.0))
        assert self.t.s() == 180.0

    def test3(self):
        Figure.fixed_first_point = R2Point(-3.0, 4.0)
        Figure.fixed_last_point = R2Point(2.0, 1.0)
        self.t = self.t.add(R2Point(0.0, 0.0))
        self.t = self.t.add(R2Point(3.0, 3.0))
        self.t = self.t.add(R2Point(-2.0, 3.0))
        self.t = self.t.add(R2Point(-2.0, 0.0))
        assert self.t.s() == approx(106.9275)

    def test4(self):
        Figure.fixed_first_point = R2Point(2.0, 2.0)
        Figure.fixed_last_point = R2Point(0.0, 0.0)
        self.t = self.t.add(R2Point(0.0, 0.0))
        self.t = self.t.add(R2Point(0.0, 2.0))
        self.t = self.t.add(R2Point(2.0, 0.0))
        self.t = self.t.add(R2Point(0.0, -2.0))
        self.t = self.t.add(R2Point(1.8, -2.3))
        self.t = self.t.add(R2Point(1.5, -3.5))
        assert self.t.s() == 135.0

    def test5(self):
        Figure.fixed_first_point = R2Point(-1.0, 2.0)
        Figure.fixed_last_point = R2Point(1.0, 0.0)
        self.t = self.t.add(R2Point(-1.0, 0.0))
        self.t = self.t.add(R2Point(-1.0, 1.0))
        self.t = self.t.add(R2Point(1.0, 2.0))
        self.t = self.t.add(R2Point(-2.0, 1.9))
        self.t = self.t.add(R2Point(-1.0, 3.0))
        self.t = self.t.add(R2Point(0.0, 4.0))
        self.t = self.t.add(R2Point(3.0, 1.0))
        self.t = self.t.add(R2Point(1.0, 0.0))
        assert self.t.s() == approx(116.565)

    def test6(self):
        Figure.fixed_first_point = R2Point(1.0, 1.0)
        Figure.fixed_last_point = R2Point(5.0, 1.0)
        self.t = self.t.add(R2Point(0.0, 1.0))
        self.t = self.t.add(R2Point(6.0, 1.0))
        self.t = self.t.add(R2Point(0.0, -5.0))
        self.t = self.t.add(R2Point(6.0, -5.0))
        assert self.t.s() == 0.0

    def test7(self):
        Figure.fixed_first_point = R2Point(-40.0, 15.0)
        Figure.fixed_last_point = R2Point(40.0, 5.0)
        self.t = self.t.add(R2Point(-20.0, 0.0))
        self.t = self.t.add(R2Point(-30.0, 20.0))
        self.t = self.t.add(R2Point(-5.0, 5.0))
        self.t = self.t.add(R2Point(20.0, 20.0))
        self.t = self.t.add(R2Point(20.0, 0.0))
        assert self.t.s() == approx(139.1849)
