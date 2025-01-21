def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

if __name__ == '__main__':
    n = int(input())
    cascade(n)