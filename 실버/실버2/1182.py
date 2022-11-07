def dfs(x, sm):
    global count
    if x == n:
        if sm == s:
            count += 1
        return
    
    dfs(x + 1, sm + tem[x])
    dfs(x + 1, sm)

n, s = map(int, input().split())
tem = list(map(int, input().split()))
count = 0
dfs(0, 0)
if s == 0:
    count -= 1
print(count)