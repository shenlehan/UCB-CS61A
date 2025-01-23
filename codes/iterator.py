a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]

def compare1():
    return all([x == y for x, y in zip(a, reversed(b))])

def compare2():
    for m, n in zip(a, reversed(b)):
        if m != n:
            return False
    return True     

def compare3():
    it1 = iter(a)
    it2 = iter(reversed(b))    
    for x, y in zip(it1, it2):
        print(x, y)

print(compare2())
print(compare1())
compare3()