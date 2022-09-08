# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

user_input_num = int(input("Введите число: "))
sum_num = 1
for elements_num in range (1,user_input_num + 1):
    sum_num*= elements_num
    print (sum_num)