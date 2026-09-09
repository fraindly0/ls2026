# # in - оператор принадлежит
# # print(" world " in "hello world")
# # print([1,2,3,4,5,6]) #list
# a = {"key" : "value","key1": "value1"}
# print("key" in a) # ищем по ключу
#  # set tuple
#  print(6 in {1,2,3,4,5,6}) #итерируимые объукты
#  print(6 in {1,2,3,4,5,6})
# print(not in)
# is / is not
# a = 10
# b = a
# print(a is b)
# a = 5
# b = 5.0
# print(a == b)
# a = 3
# b = 8
# print(a < b)
# x = True
# y = False
# print(x or y)
# num = 5
# num1 = 12
# num += 10
# print(num1 == num , num > num1 )
# a = int(input())
# b = int(input())
# print(a,b)
# print(a == b)
# import math # вариант 1
# result = math.sqrt(16)
# print(result)
# from math import sqrt
# print(sqrt(16))
# from math import (sqrt, ceil, floor , pi, log2)
# sqrt - корень от числа
# import math
# from random import lognormvariate
# print(math.radians(90))
# print(math.radians(math.pi))

# from import random random, uniform
# print(random())
# print(uniform(2.5 , 5.5)) #число от a до b дробное
# print(random(2,10)) #число от a до b целоев
# выбрать случайное чётное чисо от 0 до 20
# print(randrange(0 ,20 ,2))
# from random import shuffle, result
# # fruits = ['fh,ep', "banan","pomidor"]
# # #result = choice(fruits)
# # result = choices(fruits, k = 2)
# nums = [1,2,3,4,5,6,7,8,9,10]
# # result =sample(nums,3)
# shuffle(nums)
# print(nums)
# print((int("num", base)))# переод num из системы base
# s = bin(20) # восмеричное система счислене
# s = hex(20) # шестнацеричное повтороние
# s = bin(20)[2:]
# s = format(20,"x")
print(f'{20:b}')