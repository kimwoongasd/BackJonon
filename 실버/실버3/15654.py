def dfs(L):
    if L == m:
        print(*res)
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = tem[i]
                dfs(L + 1)
                ch[i] = 0

n, m = map(int, input().split())

tem = list(map(int, input().split()))
tem.sort()

ch = [0] * n
res = [0] * m
dfs(0)

# 함수사용
# from itertools import permutations

# n, m = map(int, input().split())
# tem = list(map(int, input().split()))
# tem.sort()

# for x in permutations(tem, m):
#     print(*x)