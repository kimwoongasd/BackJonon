def dfs(x):
    if x == m:
        print(*res)
    else:
        for i in range(n):
            res[x] = tem[i]
            dfs(x + 1)

n, m = map(int, input().split())
tem = list(map(int, input().split()))
tem.sort()

res = [0] * m
dfs(0)

# 함수 사용
# from itertools import product

# n, m = map(int, input().split())
# tem = list(map(int, input().split()))
# tem.sort()

# for x in product(tem, repeat=m):
#     print(*x)