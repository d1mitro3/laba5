from time import perf_counter
from mpmath import mp
from concurrent.futures import ThreadPoolExecutor

def kakashka(pi):
    for digit in pi:
        yield int(digit) / (int(digit) ** 2) if int(digit) != 0 else 0

mp.dps = 100000 
pi = str(mp.pi).replace(".", "")  

def process():
    result = map(sum, map(kakashka, [pi]))
    return list(result)[0]

start = perf_counter()

with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(process)

finish = perf_counter()

print(f'Время выполнения: {finish-start}\nРезультат: {future.result()}')