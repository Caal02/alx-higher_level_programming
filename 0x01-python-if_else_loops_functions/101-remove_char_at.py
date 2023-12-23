#!/usr/bin/python3
def remove_char_at(str, n):
    a = len(str)
    b = len(str)
    emp = ""
    for i in str:
        c = a - b
        b = b - 1
        i = ord(i)
        if c == n:
            continue
        i = chr(i)
# print("{}".format(i), end='') (don't use this in each loop
# since it is used in the main code)
        emp = emp + i
    return emp
