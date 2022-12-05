#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lno = number * -1
    lno = (lno % 10) * -1
else:
    lno = (number % 10)
print('Last digit of {} is'.format(number), end=" ")
if (lno > 5):
    print("{} and is greater than 5".format(lno))
elif (lno == 0):
    print("{} and is 0".format(lno))
elif ((lno < 6) and (lno != 0)):
    print('{} and is less than 6 and not 0'.format(lno))
