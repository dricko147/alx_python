#!/usr/bin/python3
# 4-square.py
# dricko147
"""Define a Class Square."""

class Square():
    """Define a private attribute size"""
    def __init__(self, size=0):
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    

    """getter method that return the size"""
    @property
    def size(self):
        return self.__size
    

    """"setter method that set a new value"""
    @size.setter
    def size(self, value):
        if not isinstance(value,int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    """Define instance method area"""
    def area(self):
        return self.__size * self.__size
    

    """Define my print method that prints in stdout the square with the character '#' """
    def my_print(self):
        if self.__size == 0:
            print("")
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print()