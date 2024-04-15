import pytest
from mpmath import mp
from time import perf_counter

def kakashka(pi):
    for digit in pi:
        yield int(digit) / (int(digit) ** 2) if int(digit) != 0 else 0

mp.dps = 100000
pi = str(mp.pi).replace(".", "")  
start = perf_counter()
print("Результат: ",*map(sum, map(kakashka, [pi])))
finish = perf_counter()
print(f'Время выполнения: {finish-start}')