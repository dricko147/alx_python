#!/usr/bin/python3
import random
number = random.randint(-10, 10)
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")