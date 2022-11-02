n = int(input())

ch = [0] * 1002
ch[1] = 1
ch[2] = 2

for i in range(3, 1002):
    ch[i] = ((ch[i - 1] + ch[i - 2]) % 10007)

print(ch[n])