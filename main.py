import math
import pytest

def test_kakashka():
    wtf = [0.3333333333333333, 1.0, 0.25, 1.0, 0.2, 0.1111111111111111, 0.5, 0.16666666666666666, 0.2, 0.3333333333333333, 0.2, 0.125, 0.1111111111111111, 0.14285714285714285, 0.1111111111111111, 0.3333333333333333]
    assert wtf == list(kakashka())
    #print()

def test2_kakashka():
    wtf = 5.117857142857142
    assert wtf == sum(kakashka())

def kakashka():
    pi = str(math.pi).replace(".", "")  # Генерируем число π и убираем десятичную точку
    for digit in pi:
        yield int(digit) / (int(digit) ** 2)  # Возвращаем результат деления цифры на её квадрат


#result = sum(kakashka())
#print("Сумма значений:", result)