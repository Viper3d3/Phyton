# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

arr = [2, 3, 5, 6]

arr_result = []

if (len(arr)) % 2 == 0:
    for i in range(len(arr)//2):
        product = arr[i] * arr[len(arr) - (i + 1)]
        arr_result.append(product)
else:
    for i in range(len(arr)//2 + 1):
        product = arr[i] * arr[len(arr) - (i + 1)]
        arr_result.append(product)      
print(arr_result)
    
