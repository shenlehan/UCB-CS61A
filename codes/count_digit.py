def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    all_but_last, last = split(n)
    return sum_digits(all_but_last) + last

if __name__ == '__main__':
    n = int(input())
    print(sum_digits(n))