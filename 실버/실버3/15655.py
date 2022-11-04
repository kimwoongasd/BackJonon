def dfs(x, L):
    if L == m:
        print(*res)
    else:
        for i in range(x, n):
            res[L] = tem[i]
            dfs(i + 1, L + 1)

n, m = map(int ,input().split())
tem = list(map(int, input().split()))
tem.sort()
res = [0] * m
dfs(0, 0)

# 함수 사용
# from itertools import combinations

# n, m = map(int ,input().split())
# tem = list(map(int, input().split()))
# tem.sort()
# for x in combinations(tem, m):
#     print(*x)