#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Figure, Void

print("Начало отрезка: ")
a = R2Point()
print("Конец отрезка: ")
b = R2Point()
Figure.fixed_first_point = a
Figure.fixed_last_point = b
f = Void()
try:
    print("Вводите координаты вершин выпуклой оболочки: ")
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, A = {f.s()}\n")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
