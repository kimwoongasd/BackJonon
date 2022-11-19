n = int(input())
ch = [0] * (n + 4)
ch[0] = 1
ch[1] = 3

for i in range(2, n + 1):
    ch[i] = ((ch[i - 1] * 2) + ch[i - 2]) % 9901
print(ch[n])