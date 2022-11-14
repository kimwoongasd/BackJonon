ch = [0] * 10001

for i in range(2, 10001):
    if ch[i] == 0:
        for j in range(i * 2, 10001, i):
            ch[j] = 1

t = int(input())

for i in range(t):
    n = int(input())
    h = n // 2
    
    for j in range(h, 1, -1):
        if ch[j] == 0 and ch[n - j] == 0:
            print(j, n - j)
            break
