"""
Определить индексы элементов массива (списка), значения которых принадлежат заданному
диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""

def find_indices(lst, min_val, max_val):
    indices = []
    for i in range(len(lst)):
        if lst[i] >= min_val and lst[i] <= max_val:
            indices.append(i)
    return indices

# Ввод длины списка
length = int(input("Введите длину списка: "))

# Ввод значений списка
print("Введите значения списка:")
values = []
for _ in range(length):
    value = int(input())
    values.append(value)

# Ввод минимального и максимального значения
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

# Поиск индексов элементов в диапазоне
result_indices = find_indices(values, min_val, max_val)

# Вывод списка
print("Список элементов:")
for value in values:
    print(value, end=" ")

# Вывод индексов элементов в диапазоне
print("\nИндексы элементов в диапазоне", min_val, "-", max_val, ":")
for index in result_indices:
    print(index, end=" ")


