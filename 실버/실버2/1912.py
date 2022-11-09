n = int(input())
tem = list(map(int, input().split()))
ch = [0] * n
ch[0] = tem[0]
for i in range(1, n):
    ch[i] = max(ch[i - 1] + tem[i], tem[i])
print(max(ch))