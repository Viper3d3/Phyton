# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

a = [1, 1, 2, 3, 4, 5, 5, 6]
lst = []
for i in a:
    if a.count(i) == 1:
        lst.append(i)
print(lst)

