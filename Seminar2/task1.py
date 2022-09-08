# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

numbers = input("Введите вещественно число:")
numbers_cleared = numbers.replace(",", "").replace(".", "")
summ = 0
for i in numbers_cleared:
    i = int(i)
    summ+= i
print(summ)