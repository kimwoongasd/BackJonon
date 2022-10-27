n = int(input())

ch = [0] * (n + 2)
ch[1] = 1
ch[2] = 2

for i in range(3, n + 1):
    ch[i] = (ch[i - 1] + ch[i - 2]) % 15746

print(ch[n])