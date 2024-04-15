import pytest
from mpmath import mp

def test_kakashka():
    wtf = 28381.848412703097
    assert wtf == list(map(sum, map(kakashka, [pi])))[0]
def kakashka(pi):
    for digit in pi:
        yield int(digit) / (int(digit) ** 2) if int(digit) != 0 else 0

mp.dps = 100000
pi = str(mp.pi).replace(".", "")  
print()