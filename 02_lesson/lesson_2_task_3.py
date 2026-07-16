from math import ceil


def square(a):
    return ceil(a*a)


a = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата - {square(a)}.")
