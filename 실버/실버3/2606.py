def DFS(x):
    global count
    for i in range(1, n + 1):
        if ch[i] == 0 and cpu[x][i] == 1:
            ch[i] = 1
            count += 1
            DFS(i)

n = int(input())
t = int(input())

ch = [0] * (n + 1)
cpu = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(t):
    a, b = map(int, input().split())
    cpu[a][b] = 1
    cpu[b][a] = 1
ch[1] = 1
count = 0
DFS(1)
print(count)