def absolute_value(x):
    """return the absolute value of x"""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
    
a = int(input())
print('absolute value of a is', absolute_value(a))