# # Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# # Пример:

# # - A (3,6); B (2,1) -> 5,09
# # - A (7,-5); B (1,-1) -> 7,21

import math
coordinate_a = [3,6]
coordinate_b = [2, 1]
distance = math.sqrt( ((coordinate_a[0]-coordinate_b[0])**2)+((coordinate_a[1]-coordinate_b[1])**2) )
print(distance)

