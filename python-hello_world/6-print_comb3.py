for a in range(10):
    for b in range(a + 1, 10):

        if a == 8 and b == 9:
            print("{:01d}{:01d}".format(a, b), end="")
        else:
            print("{:01d}{:01d}".format(a, b), end=", ")
print()