# Есть словарь dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
# Составить из него новый словарь, содержащий только те элементы, у которых значение больше или равно 3.

a = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
b ={}

for k, v in a.items():
    if (v >= 3): b[k] = v

print(b)