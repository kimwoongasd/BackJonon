def dfs(x):
    if x == m:
        print(*res)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[x] = i
                dfs(x + 1)
                ch[i] = 0

n, m = map(int, input().split())

ch = [0] * (n + 1)
res = [0] * m
dfs(0)

# 함수사용
# from itertools import permutations
# n, m = map(int, input().split())
# ch = [i for i in range(1, n + 1)]

# for x in permutations(ch, m):
#     print(*x)