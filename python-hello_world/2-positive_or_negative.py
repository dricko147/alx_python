#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = float(input("Enter a number: "))
if number > 0:
   print("Positive number")
elif number == 0:
   print("Zero")
else:
   print("Negative number")