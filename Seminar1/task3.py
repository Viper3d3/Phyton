# # Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# # Пример:

# # - x=34; y=-30 -> 4
# # - x=2; y=4-> 2
# # - x=-34; y=-30 -> 3

coordinate_x = int(input("Введите координату Х:"))
coordinate_y = int(input("Введите координату Y:"))

if coordinate_x > 0 and coordinate_y > 0:
    print("Это первая четверть")
elif coordinate_x < 0 and coordinate_y > 0:
    print("Это вторая четверть")
elif coordinate_x < 0 and coordinate_y < 0:
    print("Это третия четверть")
elif coordinate_x > 0 and coordinate_y < 0:
    print("Это четвертая четверть")
