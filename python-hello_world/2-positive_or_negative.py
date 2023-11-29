#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
  print ("a{number}is positive")
elif number == 0:
  print ("a{number}is zero")
else:
  print ("a{number}is < 0")