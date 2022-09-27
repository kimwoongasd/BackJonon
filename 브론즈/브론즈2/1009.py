import sys
n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10
    
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print((a * a) % 10)
        else:
            print(a)
    else:
        if b % 4 == 0:
            print((a ** 4) % 10)
        else:
            print((a ** (b % 4)) % 10)
        