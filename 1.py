# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3
#  и 9, ответ: 12

n=[1, 2, 3, 4, 5]
l=len(n)
even=[]
odd=[]
for i in range(l):
    if i%2==0:
        even.append(n[i])
    else:
        odd.append(n[i])
print(f"even position elements:{even}, odd position elements: {odd}")
print(sum(even))