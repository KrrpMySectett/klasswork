# -*- coding: utf-8 -*-
#Задание 1
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
if a > b:
    maximum = a
    minimum = b
else:
    maximum = b
    minimum = a
print("Максимальное число: ", maximum)
print("Минимальное число: ", minimum)

#Задание 2
a = int(input("Введите сторону: "))
b = int(input("Введите радиус: "))
if a > b:
    print("Круг влез: ")
else:
    print("Круг невлез: ")

#Задание 4
a = int(input("Введите сторону: "))
b = int(input("Введите радиус: "))
if a < b:
    print("Квадрат влез: ")
else:
    print("Квадрат невлез: ")

#Задание 5
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print("Первое число больше")
else:
    print("Второе число больше")