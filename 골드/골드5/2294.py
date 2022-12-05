n, k = map(int, input().split())
coin = []
for i in range(n):
    a = int(input())
    coin.append(a)

ch = [2174000000] * (k + 1)
ch[0] = 0
for i in coin:
    for j in range(i, k + 1):
        ch[j] = min(ch[j], ch[j - i] + 1)    
        
if ch[k] == 2174000000:
    print(-1)
else:
    print(ch[k])
