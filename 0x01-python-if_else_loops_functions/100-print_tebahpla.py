#!/usr/bin/python3
n = 25
for i in range(65, 91):
    if i % 2 != 0:
        i = i + 32
    i = i + n
    i = chr(i)
    print(i, end='')
    n = n - 2
