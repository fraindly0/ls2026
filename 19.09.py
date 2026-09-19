# from math import log2
# res = 1024 * 768
# bitrate = 1310720
# N = 4096
# t = 300
# i = log2(N)
# img_size = res * i
# package_size = bitrate * t
# img_in_package = package_size // img_size
# print(img_in_package)

# from math import log2, ceil
# res = 2764 * 1793
# N = 7026
# bet = 18349566
# img_in_package = 148
# i = ceil(log2(N))
# img_size = res * i
# package_size = img_size * img_in_package
# time = package_size // bet
# print(time)

# from math import log2 , ceil
# res = 1024 * 960
# N = 16384
# img_in_package = 400
# i = log2(N)
# img_size = res * i
# package_size = img_size * img_in_package / 8 / 1024 / 1024
# print(int(package_size))

# from math import log2,ceil
# res = 512 * 750
# memory_size = 80 * 2 ** 13
# i = memory_size//(res * 0.65)
# N = 2 ** i
# print(N)

# from math import log2, ceil
# res = 2560 * 5040
# memory_size = 14175 * 2 ** 13
# i = memory_size // res
# N = 2 ** i
# print(N)

# from math import log2, ceil
# res = 1024 * 960
# t = 140
# betrait = 1474560
# img_in_package = 32
# memory_size = betrait * t
# img_size = pacage_size / img_in_package
# N = 2 ** i
# print(N)
from math import log2, ceil
res1 = 1024 * 768
res2 = 800 * 600
N = 223
i = ceil(log2(N))
img_in_package = 100
img_size1 = res1 * i
img_size2 = res2 * i
pocage_size =