#!/usr/bin/python3
# 4-square.py
# dricko147
"""Define a class Square."""


class Square:
   def __init__(self, size=0):
        self.size = size @property

def size(self):
        return self.__size 
    
@size.setter
def size(self, value):
        if not isinstance(value,int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
def area(self):
        return self.__size ** 2
    
def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
                
if __name__=="__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")