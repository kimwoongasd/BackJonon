def dfs(x, L):
    if L == m:
        print(*res)
    else:
        for i in range(x, n + 1):
            res[L] = i
            dfs(i, L + 1)


n, m = map(int, input().split())

res = [0] * m
dfs(1, 0)

# 함수 사용
# from itertools import combinations_with_replacement

# n, m = map(int, input().split())
# ch = [i for i in range(1, n + 1)]

# for x in combinations_with_replacement(ch, m):
#     print(*x)# 