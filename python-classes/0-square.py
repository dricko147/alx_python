#!/usr/bin/python3
# 0-square.py
# dricko147
class Square:
    '''initializing size'''
    def __init__(self, size):
        self.__size = size
    
if __name__=="__main__":
    '''this is a module to test the class'''
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)