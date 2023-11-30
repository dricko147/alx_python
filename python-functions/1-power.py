def power(a, b):
 
    # If a^0 return 1
    if (b == 0):
        return 1
 
    # If we need to find of 0^y
    if (a == 0):
        return 0
 
    # For all other cases
    return x * power(a, b - 1)
  
# therefore
if __name__ == "__main__":
    a = 2
    b = 3
 
    # Function call
    print(power(a, b))