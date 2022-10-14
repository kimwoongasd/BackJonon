n = list(input())

tem = [0 for _ in range(10)]
count = 0

for x in n:
    if int(x) == 9:
        tem[int(6)] += 1
    else:
        tem[int(x)] += 1

tem[6] = (tem[6] + 1) // 2
print(max(tem))
