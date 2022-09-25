a, b = map(int, input().split())
c = int(input())

x = b + c

if x >= 60:
    a += x // 60
    x = x % 60

if a >= 24:
    a = a % 24
print(f"{a} {x}")