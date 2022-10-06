tem = []

for _ in range(9):
    a = int(input())
    tem.append(a)

for i in range(8):
    for j in range(i + 1, 9):
        if sum(tem) - tem[i] - tem[j] == 100:
            tem[i] = 0
            tem[j] = 0
            break
    if sum(tem) == 100:
        break

res = []
for x in tem:
    if x != 0:
        res.append(x)
res.sort()
for x in res:
    print(x)
