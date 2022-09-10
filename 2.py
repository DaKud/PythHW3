# Напишите программу, которая найдёт произведение пар 
# чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.
# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
sum1 = list[0] + list[-1]
sum2 = list[1] + list [3]
print(f"Sum of the 1st element and the last one = {sum1},Sum of the 2nd element and the third = {sum2} ")