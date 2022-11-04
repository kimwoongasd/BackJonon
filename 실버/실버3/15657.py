def dfs(x, L):
    if L == m:
        print(*res)
    else:
        for i in range(x, n):
            res[L] = tem[i]
            dfs(i, L + 1)

n ,m = map(int, input().split())
tem = list(map(int, input().split()))
tem.sort()

res = [0] * m
dfs(0, 0)

# 함수사용
# from itertools import combinations_with_replacement

# n ,m = map(int, input().split())
# tem = list(map(int, input().split()))
# tem.sort()

# for x in combinations_with_replacement(tem, m):
#     print(*x)