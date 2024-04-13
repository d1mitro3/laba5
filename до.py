import math
from time import perf_counter

def kakashka():
    pi = str(math.pi).replace(".", "")  # Генерируем число π и убираем десятичную точку
    for digit in pi:
        yield int(digit) / (int(digit) ** 2)  # Возвращаем результат деления цифры на её квадрат

start = perf_counter()
result = sum(kakashka())
finish = perf_counter()
print(f'Время выполнения: {finish-start}\nРезультат: {result}')