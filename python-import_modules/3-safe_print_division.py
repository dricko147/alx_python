def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        result = None
    finally:
        print('Inside result: {}'.format(result))
        return result
    
if __name__=='__main__':
    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{} / {} = {} ".format(a, b, result))
        