def dfs(s, L):
    if L == m:
        print(*res)
    else:
        t = 0
        for i in range(s, n):
            if ch[i] == 0 and t != arr[i]:
                ch[i] = 1
                t = arr[i]
                res[L] = arr[i]
                dfs(i + 1, L + 1)
                ch[i] = 0

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ch = [0] * n
res = [0] * m
dfs(0, 0)


# itertools 사용
# 약간 더 빠름
# from itertools import combinations

# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# res = sorted(list(set(combinations(arr, m))))
# for x in res:
#     print(*x)