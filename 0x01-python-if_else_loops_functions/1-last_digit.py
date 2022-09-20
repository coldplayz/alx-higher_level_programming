#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg2pos = -1
if number < 0:
    neg2pos = number * (-1)
    neg2pos = neg2pos % 10
last = number % 10

if neg2pos != -1:
    print(f"Last digit of {number} is {-neg2pos}", end=' ')
else:
    print(f"Last digit of {number} is {last}", end=' ')

if neg2pos != -1:
    print("and is less than 6 and not 0")
elif last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
elif 6 > last != 0:
    print("and is less than 6 and not 0")
