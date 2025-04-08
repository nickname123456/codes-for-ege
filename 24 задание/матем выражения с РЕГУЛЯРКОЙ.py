# 7497
from re import *

s = open('24-298.txt').readline()
num=r'([1-9][0-9]*)'
reg = rf'{num}([*-]{num})+'

m=(max( [x.group() for x in finditer(reg, s)], key=len  ))
print(len(m))