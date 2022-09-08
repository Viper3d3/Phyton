# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

import random

N = int(input("Введите число: "))
array_list = [0] * N
for i in range(N):
    array_list[i] = random.randint(-N, N)  
print(array_list)

input_user = input("Введите числа через пробел: ")
current_user_input = input_user.split()
for i in range(len(current_user_input)):
    current_user_input[i] = int(current_user_input[i])
 
print(current_user_input) 

multi = 1
for i in current_user_input:
    multi *= array_list[i - 1]
print(multi)