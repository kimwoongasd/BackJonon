a = input()
b = input()

ch = [[0] * (len(a) + 1) for _ in range(len(b)+ 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if b[i - 1] == a[j - 1]:
            ch[i][j] = ch[i - 1][j - 1] + 1
        else:
            ch[i][j] = max(ch[i - 1][j], ch[i][j - 1])
print(ch[len(b)][len(a)])