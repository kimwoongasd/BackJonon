n = int(input())
ch = [0] * 301

for i in range(1, n + 1):
    ch[i] = int(input())

count = [0] * 301

count[1] = ch[1]
count[2] = ch[1] + ch[2]
count[3] = max(ch[1] + ch[3], ch[2] + ch[3])

for i in range(4, n + 1):
    count[i] = max(count[i - 3] + ch[i] + ch[i - 1], count[i - 2] + ch[i])

print(count[n])
