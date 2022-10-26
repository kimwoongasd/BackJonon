n = int(input())
tem = list(map(int, input().split()))
tem.sort()

for i in range(1, n):
    tem[i] = tem[i - 1] + tem[i]

print(sum(tem))