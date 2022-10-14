m = int(input())
n = int(input())

tem = [0] * (n + 1)
tem[1] = 1
ls = []
for i in range(2, n + 1):
    if tem[i] == 0:
        for j in range(i * 2, n + 1, i):
            tem[j] = 1

for k in range(m, n + 1):
    if tem[k] == 0:
        ls.append(k)
if len(ls) != 0:
    print(sum(ls))
    print(min(ls))
else:
    print(-1)