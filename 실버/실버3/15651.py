def dfs(x):
    if x == m:
        print(*res)
    else:
        for i in range(1, n + 1):
            res[x] = i
            dfs(x + 1)

n, m = map(int, input().split())

res = [0] * m
dfs(0)

# 함수사용
# from itertools import product
# n, m = map(int, input().split())

# ch = [i for i in range(1, n + 1)]
# for x in product(ch, m):
#     print(*x)