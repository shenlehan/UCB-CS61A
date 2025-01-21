from operator import mul

def trace1(fn):
    def traced(x):
        print('Calling ', fn, 'on argument ', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return mul(x, x)

@trace1
def sum_squares_up_to_n(n):
    k, sum = 1, 0
    while k <= n:
        sum, k = sum + square(k), k + 1
    return sum

if __name__ == '__main__':
    print(sum_squares_up_to_n(10))