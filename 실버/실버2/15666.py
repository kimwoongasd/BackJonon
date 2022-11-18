def dfs(s, L):
    if L == m:
        print(*res)
    else:
        t = 0
        for i in range(s, n):
            if t != arr[i]:
                res[L] = arr[i]
                t = arr[i]
                dfs(i, L + 1)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = [0] * m
dfs(0, 0)

# itertools 사용
# 더 빠름
# from itertools import combinations_with_replacement
# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# res = sorted(list(set(combinations_with_replacement(arr, m))))
# for x in res:
#     print(*x)