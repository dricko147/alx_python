#!/usr/bin/python3
# 2-square.py
# dricko147

"""Define a Square Class."""
class Square():
    """Define a private attribute size"""
    def __init__(self, size=0):
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    

    """Define instance method area"""
    def area(self):
        return self.__size * self.__size
    