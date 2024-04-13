import math
from concurrent.futures import ThreadPoolExecutor as executor
from time import perf_counter

def kakashka(digit):
    return int(digit) / (int(digit) ** 2) 

start = perf_counter()
result = sum(executor().map(kakashka, str(math.pi).replace(".", "")))
finish = perf_counter()

print(f'Время выполнения: {finish-start}\nРезультат: {result}')