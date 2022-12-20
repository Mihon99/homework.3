# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# 
# n = int(input('Введите длину списка: '))
# list = []
# sum = 0
# for e in range(n):
    # list.append(random.randint(1, 9))
# 
# print(list)
# print('Сумма элементов', end = ' ')
# for i in range(len(list)):
    # if i % 2 != 0:
        # sum += list[i]
        # print(list[i], end = ' ')
# 
# print(f'на нечетных позициях = {sum}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import random
# 
# n = int(input('Введите длину списка: '))
# list = []
# list2 = []
# for i in range(n):
    # list.append(random.randint(1, 9))
# 
# for e in range(len(list)):
    # while e < len(list)/2 and n > len(list)/2:
        # a = list[e] * list[n-1]
        # list2.append(a)
        # n -= 1
        # e += 1
        # 
# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(lst)
# print(new_lst)
# print(max(new_lst) - min(new_lst))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input('Введите число в десятичной системе исчесления которое хотите перевести в двоичную систему исчисления: '))
# s = ''
# 
# while number != 0:
    # s += str(number%2)
    # number //= 2
    # print(s)
    # print(number)
# 
# print(s)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# n = int(input('Введите число: '))
# 
# def get_fibonacci(n):
    # fibo_numbers = []
    # a, b = 1, 1
    # 
    # for i in range(n):
        # fibo_numbers.append(a)
        # a, b = b, a + b
    # a, b = 0, 1
    # for i in range(n+1):
        # fibo_numbers.insert(0, a)
        # a, b = b, a - b
    # return fibo_numbers
# 
# fibo_numbers = get_fibonacci(n)
# print(get_fibonacci(n))