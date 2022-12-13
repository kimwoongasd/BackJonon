# 2293문제와 비슷하다
t = int(input())
for _ in range(t):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    ch = [0] * (m + 1)
    ch[0] = 1
    
    for x in coin:
        for i in range(1, m + 1):
            if i - x >= 0:
                ch[i] += ch[i - x]
    print(ch[m])