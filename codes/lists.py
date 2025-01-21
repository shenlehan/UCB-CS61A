from operator import add, mul

digits = [1, 2, 4, 8]
print(digits.__len__())
print(len(digits))
print(add([3, 5], mul(2, digits)))

print(1 in digits)

for i in digits:
    print(i, end=" ")
print("")

pairs = [[1, 2], [3, 3], [4, 5], [4, 4]]
for x, y in pairs: # automatic unpacking
    if x == y:
        print('Same!')

odds = [1, 3, 5, 7, 9, 11]
print([x + 1 for x in odds if 25 % x == 0])

# slice
print(odds[:3])
print(odds[1:])
print(odds[:])

# sum
print(sum(odds))

# max
print(min(odds, key=lambda x: (x - 1) * (x - 7)))

#exec
command = 'print(add(1, 2))'
print(command)
exec(command)