# # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# # Пример:

# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет

# # 1 решение 
# day = int(input("Введите день недели:"))                     
# if day == 1:
#     print(f"Он не является выходным днем.")
# elif day == 2:
#     print(f"Он не является выходным днем.")
# elif day == 3:
#     print(f"Он не является выходным днем.")
# elif day == 4:
#     print(f"Он не является выходным днем.")
# elif day == 5:
#     print(f"Он не является выходным днем.")
# elif day == 6:
#     print(f"Этот день Суббота, он является выходным днем.")
# elif day == 7:
#     print(f"Этот день Воскресенье, он является выходным днем.")

# # 2 решение 

# dayOfWeak = int(input("Введите день недели от 1 до 7:"))
# if dayOfWeak in [1,2,3,4,5]:
#     print("Будний день!")
# else:
#     print("Выходной день!")





























