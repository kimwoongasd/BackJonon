tem = []

for _ in range(9):
    a = int(input())
    tem.append(a)

for i in range(8):
    s = tem[i]
    total = sum(tem) - s
    tem[i] = 0
    for j in range(i + 1, 9):
        if total - tem[j] == 0:
            tem[j] = 0
            break
        else:
            if total - tem[j] < 100:
                break
            
    if sum(tem) == 0:
        break
    else:
        tem[i] = s

res = []
for i in range(9):
    if tem[i] != 0:
        res.append(tem[i])
res.sort()

for x in res:
    print(x)