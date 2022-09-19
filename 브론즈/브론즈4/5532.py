# import math

# L = int(input())
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# x = math.ceil(a / c)
# y = math.ceil(b / d)
# m = max(x, y)
# print(L - m)

L = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

x = 0
y = 0
if a % c == 0:
    x = a //c
else:
    x = a // c + 1
    
if b % d == 0:
    y = b // d
else:
    y = b // d + 1

print(L - max(x, y))