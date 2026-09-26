# time = 42 * 60 + 30
# k = 2
# n = 44 * 1000
# bitrate = 295905280
# tracks = 12
# header = 110 * 1024 * 8
# i = 16
# v = time * i * n * k
# V_a = v + header * 12
# q = V_a // bitrate
# print(q)

# t =7 * 60
# i = 32
# k = 4
# n = 44000
# prop = 3 * 1024 * 8
# v = t * n * k * i
# V_a = v // prop // 3600
# print(V_a)
#
# t = 49 * 60
# bitraid = 245839600
# tracks = 7
# n = 48 * 1000
# i = 16
# k = 2
# header = 55 * 1024 * 8
# v = t * i * n * k
# V_a = v + header * 12
# q = V_a // bitraid
# print(q)

# from math import floor
# time = 35 * 60 + 50
# k = 2
# n = 20000
# i = 32
# v_al = 339 * 1024 * 1024 * 8
# tracks = 13
# v = k * time * i * n
# header_kb = (v_al - v) / 13
# header = header_kb / 8 / 1024
# print(floor(header))

# from math import ceil
# time = 2 * 60 + 20
# k = 2
# n = 28000
# i = 8
# v = k * time * i * n
# v_all = v / 8 / 1024
# print(ceil(v_all))

from math import ceil
# time = 4 * 60 + 18
# n = 20000
# i = 16
# k = 1
# v = time * i * n * k
# v_all = v / 1024 / 1024 / 8
# print(floor(v_all))

# i = 16
# time = 3 * 60 + 10
# n = 12000
# k = 1
# v = time * i * n * k
# v_all = v / 1024 / 1024 / 8
# print(ceil(v_all))

# print(39 * 4 * 2.5 / 2)

t = 2 * 60 + 30
n = 48000
i = 32
k = 2
bitraid = 1280000
i_compresed = 16
n_compresed = 32000
v = t * n * i * k
v_compresed = t * n * i_compresed * k * n_compresed
