import sys
input = sys.stdin.readline

ch = [0] * 1000001
for i in range(2, 1000001):
    if ch[i] == 0:
        for j in range(i * 2, 1000001, i):
            ch[j] = 1

while True:
    a = int(input())
    if a == 0:
        break
    
    for i in range(3, a // 2 + 1):
        if ch[i] == 0 and ch[a - i] == 0:
            print(f"{a} = {i} + {a - i}")
            break
    else:
        print("Goldbach's conjecture is wrong.")