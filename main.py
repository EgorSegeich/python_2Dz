# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('введите число монеток '))
# orel = 0
# reshka = 0

# for _ in range(n):
#     a = int(input('введите 1 или 0 (1 - орёл, 0 - решка) '))
#     if a == 1:
#         orel = orel + 1
#     if a == 0:
#         reshka = reshka +1
#     if a > 1:
#         print("введено некорректное значение")
#
# if orel <= reshka:
#     print(orel)
# else:
#     print('минимальное количество монет, которые нужно перевернуть = ', reshka)





# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# x = int(input('введите сумму чисел '))
# y = int(input('введите произведение чисел '))
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print("искомые числа: ", i, j)




# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
#
# n = int(input('введите число N '))
# summ = 0
# k = 0
#
# while n > summ:
#     summ = 2**k
#     if n >= summ:
#         print(summ)
#     k = k + 1