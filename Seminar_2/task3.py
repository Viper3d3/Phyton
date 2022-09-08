# Задайте список из k=5 чисел последовательности (1 + 1\k)**k и выведите на экран их сумму.

k = int(input("Введите число:"))
sum = 0
for current_k in range(1, k + 1):
    sum += (1+1/current_k)**current_k
print(sum)