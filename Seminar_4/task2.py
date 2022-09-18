# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

num = int(input("Введите число: "))
i = 2 
list_1 = []
temp = num
while i <= num:
    if num % i == 0:
        list_1.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(list_1)