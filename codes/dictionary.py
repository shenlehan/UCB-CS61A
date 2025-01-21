numerals = {'I': 1, 'v': 5, 'X': 10}

for key in numerals.keys():
    print(key)

new_dict = {}
new_dict["hello"] = 1
new_dict["world"] = 2
for key, value in new_dict.items():
    print(key, value)

d = {k: new_dict[k] for k in new_dict.keys() if k != 3}
print(d)