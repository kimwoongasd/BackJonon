n, w, h, l = map(int, input().split())

width = w // l
height = h // l

num = width * height

if num <= n:
    print(num)
else:
    print(n)