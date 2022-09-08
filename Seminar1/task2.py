# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

myArr = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
counter = 0
for i in myArr :
    expr = (not(i[0] or i[1] or i[2])) == ((not i[0]) and (not i[1]) and (not i[2]))
    if expr == True:
        counter+=1
print(counter) 