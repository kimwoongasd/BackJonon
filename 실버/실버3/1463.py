n = int(input())
ch = [0 for _ in range(n + 1)]
count = 0
for i in range(2, n + 1):
    ch[i] = ch[i - 1] + 1
    
    if i % 3 == 0:
        ch[i] = min(ch[i // 3] + 1, ch[i])
    if i % 2 == 0:
        ch[i] = min(ch[i // 2] + 1, ch[i])


print(ch[n])

