def dfs(idx, res):
    global max_res, min_res
    
    if idx == n:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return
    
    if tem[0] > 0:
        tem[0] -= 1
        dfs(idx+1, res + num[idx])
        tem[0] += 1
    if tem[1] > 0:
        tem[1] -= 1
        dfs(idx+1, res - num[idx])
        tem[1] += 1
    if tem[2] > 0:
        tem[2] -= 1
        dfs(idx+1, res * num[idx])
        tem[2] += 1
    if tem[3] > 0:
        tem[3] -= 1
        dfs(idx+1, int(res / num[idx]))
        tem[3] += 1

n = int(input())
num = list(map(int, input().split()))
tem = list(map(int, input().split()))
max_res = -2174000000
min_res = 2174000000

dfs(1, num[0])
print(max_res)
print(min_res)