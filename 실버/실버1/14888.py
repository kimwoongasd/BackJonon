def dfs(L, t, plus, minus, multiply, divide):
    global res_min, res_max
    if L == n:
        res_min = min(res_min, t)
        res_max = max(res_max, t)
    else:
        if plus:
            dfs(L + 1, t + num[L], plus - 1, minus, multiply, divide)
        if minus:
            dfs(L + 1, t - num[L], plus, minus - 1, multiply, divide)
        if multiply:
            dfs(L + 1, t * num[L], plus, minus, multiply - 1, divide)
        if divide:
            dfs(L + 1, int(t / num[L]), plus, minus, multiply, divide - 1)

n = int(input())
num = list(map(int, input().split()))
tem = list(map(int, input().split()))

res_min = 2174000000
res_max = -2174000000
dfs(1, num[0], tem[0], tem[1], tem[2], tem[3])
print(res_max)
print(res_min)