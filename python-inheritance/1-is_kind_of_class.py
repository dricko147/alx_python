#!/usr/bin/python3
# # 1-is_kind_of_class.py
# dricko147
'''functions that inherits from'''
def inherits_from(obj, a_class):
    '''functions that check if its true it inherits from the type object'''
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)