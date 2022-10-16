#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon, Figure


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

print("Начало отрезка: ")
a = R2Point()
print("Конец отрезка: ")
b = R2Point()
Figure.fixed_first_point = a
Figure.fixed_last_point = b
f = Void()

try:
    tk.draw_line2(a, b)
    print("Вводите координаты вершин выпуклой оболочки: ")
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        tk.draw_line2(a, b)
        print(f"S = {f.area()}, P = {f.perimeter()}, A = {f.s()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
