"""calculating the fibonacci sequence"""

def fib(n):
    pred, curr = 1, 0
    k = 0
    while k < n:
        pred, curr = curr, curr + pred
        k = k + 1
    return curr

for i in range(0, 11):
    print(fib(i))