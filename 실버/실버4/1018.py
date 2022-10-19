n, m = map(int, input().split())
tem = []
ch = []
for i in range(n):
    a = list(map(str, input()))
    tem.append(a)

for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for k in range(i, i + 8):
            for p in range(j, j + 8):
                if (k + p) % 2 == 0:
                    if tem[k][p] != "W":
                        w += 1
                    if tem[k][p] != "B":
                        b += 1
                else:
                    if tem[k][p] != "B":
                        w += 1
                    if tem[k][p] != "W":
                        b += 1
        ch.append(min(w, b))
print(min(ch))