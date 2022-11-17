import sys
sys.setrecursionlimit(10**6)

def dfs(x):
    ch[x] = 1
    for i in arr[x]:
        if ch[i] == 0:
            dfs(i)

n, m = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n + 1)]
ch = [0] * (n + 1)
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

for x in arr:
    x.sort()
count = 0
for i in range(1, n + 1):
    if ch[i] == 0:
        dfs(i)
        count += 1
print(count)