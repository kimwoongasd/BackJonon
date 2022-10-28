n = int(input())
ch = [0] * (n + 2)
ch[1] = 1
ch[2] = 1

for i in range(3, n + 1):
    ch[i] = ch[i - 2] + ch[i - 1]
print(ch[n])