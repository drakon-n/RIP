#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['A', 'a', 'B', 'b', 'a', 'AB', 'aB', 'ab', 'Ba', 'Ab']
print(*Unique(data2))
print(*Unique(data3, ignore_case=True))
print(*Unique(data3, ignore_case=False))

# Реализация задания 2