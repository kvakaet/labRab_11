#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import math
import sys


def cylinder():
    """""
    Вычисление площади полной или боковой поверхности цилиндра
    """""
    while True:
        vs = int(input("Какую площадь вы хотите вычислить? (введите число):\n"
                       "1 -> Боковой поверхности\n"
                       "2 -> Полной поверхности\n"
                       ">>> "))
        if (vs != 1) and (vs != 2):
            print(f"Неизвестная комманда {vs}", file=sys.stderr)
            break

        r = int(input("Введите радиус "))
        h = int(input("Введите высоту цилиндра: "))

        if vs == 1:
            s = 2 * math.pi * r * h
            print("S(бок.) = ", '{:.3f}'.format(s))
            break

        elif vs == 2:
            s = (2 * math.pi * r * h) + (circle(r) * 2)
            print("S(полн.) = ", '{:.3f}'.format(s))
            break


def circle(r):
    """""
    Вычисление площади круга по заданному радиусу
    """""
    return math.pi * (r ** 2)


if __name__ == '__main__':
    cylinder()
