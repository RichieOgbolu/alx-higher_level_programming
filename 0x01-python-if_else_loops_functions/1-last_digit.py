#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1

info = f"Last digit of {number} is {last_digit} and is"
if last_digit == 0:
    print(info, "0")
elif last_digit > 5:
    print(info, "greater than 5")
else:
    print(info, "less than 6 and not 0")
