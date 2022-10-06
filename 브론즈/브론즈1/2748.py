n = int(input())

tem = [0] * (n + 2)
tem[1] = 1
tem[2] = 1

for i in range(3, n + 1):
    tem[i] = tem[i - 2] + tem[i - 1]

print(tem[n])