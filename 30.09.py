# from math import ceil
# k = 4
# t = 44 * 60 + 30
# bitraid = 295905280
# i = 32
# tracks = 12
# n = 44000
# header = 110 * 2 ** 13
# v = k * t * i * n
# Valbon = v + header * 13
# q = Valbon / bitraid
# print(ceil(q))

# k = 2
# n = 12000
# i = 24
# t = 3 * 60 + 19
# v = k * t * i * n
# nil = v // 8 // 1024
# print(nil)

# N - мощность алфавита
# i = log2(N)
# N = 2 ** i
# I = L * i общий вес сообщение
# L = I / i длина одного сообщение
# 5,2 -> округляе в мень

# from math import log2, ceil
# ids_size = 693 * 2 ** 10
# k = 2000
# N = 52 + 10 + 963
# i = ceil(log2(N))
# I = int(ids_size / k)
# L = I * 8/ i
# print(int(L))

from math import log2, ceil
# ids_size = 709 * 2 * 10
# k = 2050
# N =  26 + 10 + 2013
# i = ceil(log2(N))
# I = int(ids_size / k)
# L = I * 8 / i
# print(int(L))

# k = 1234567
# N = 70 + 10
# ids_size= 24 * 2 ** 20
# i = ceil(log2(N))
# I = ceil(ids_size / k)
# L = I * 8/ i
# print(int(L))

# N = 52 + 1988 + 10
# ids_size= 356 * 2 ** 10
# k = 1550
# i = ceil(log2(N))
# I = int(ids_size / k)
# L = I * 8 / i
# print(int(L))