import random
from functools import reduce
from math import factorial
# Задание: усовершенствовать код старых задач применяя lambda, list comprehension
# map, enumerate, filter, zip

#мной использованно: list comprehension, lambda, map, enumerate (filer и zip не нашёл где вставить)

# Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12




# def checking_number (num_for_check):
#     while not num_for_check.isdigit():
#         print ("it's not possitive and integer number, pls try again: ")
#         num_for_check = input("Input possitive and integer number which is quantity of elements in your list: ")
#     else:
#         return int(num_for_check)

# def create_rand_list(num_of_el):
#     rand_list=[]
#     if num_of_el == 0:
#         print ("You made empty list, my congratulations, weirdo")
#     else:

#         #было:

#         # for i in range(num_of_el):
#         #     rand_list.append(random.randint(-8,8))

#         #стало с list comprehension:

#         rand_list = [random.randint(-8,8) for _ in range(num_of_el)]
#         return rand_list

# def sum_of_the_odd_elements (iterated_list):
#     sum_el = 0
#     for i in range(1, len(iterated_list), 2):
#         sum_el +=iterated_list[i]
#     return sum_el

# user_input = checking_number(
#             input('Input possitive and integer number\
#  which is quantity of elements in your list: '))
# new_list = create_rand_list(user_input)
# print (f'it\'s your new list:\n{new_list}')
# print(f'Sum of elements in odd indexes is "{sum_of_the_odd_elements(new_list)}"')

# Задача 5 Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

#    # было у меня
#    # def fibonacci (n):
#    #     if n == 0:
#    #         leonardus=["0"]
#    #         return leonardus
#    #     else:
#    #         leonardus = [i for i in range(0, 2)]
#    #         i = 2
#    #         while i < n+1:
#    #             leonardus.append (leonardus[i-1] + leonardus[i-2])
#    #             i+=1
#    #         return leonardus

# стало с lambda, написано при помощи гугла(без reduce не получалось, хотя логика 1 в 1), но как же это просто и логично выглядит)



# def fib(n): return reduce(lambda x, _: x+[x[-1]+x[-2]],
#                           range(n-2), [0, 1])


# ask_for_number = int(input('please num for fibonacci: '))
# print(fib(ask_for_number))

# Задача 2 Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.
#    # было:
#    # def factorial_finder (input_factorial):
#    #     if input_factorial == 0:
#    #         print ("All right megabrain your F(n):")
#    #         return input_factorial + 1
#    #     else:
#    #         count = 1
#    #         n = 1
#    #         while count < input_factorial+1:
#    #             n = n * count
#    #             count = count + 1
#    #             print (f'{count-1}! = {n}')
#    #         return n
#    # стало:

# num = int(input('Input n and you\'ll find out F(n): '))
# my_list = [i for i in range (num+1)]
# my_list = list (enumerate((map(factorial, my_list))))
# print (f'your list from F(0) to F({num}) is:')
# print (*my_list)