# 함수 사용보다 빠름
def dfs(L):
    if L == m:
        print(*res)
    else:
        t = 0
        for i in range(n):
            if arr[i] != t:
                res[L] = arr[i]
                t = arr[i]
                dfs(L + 1)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = [0] * m
dfs(0)


# itertools 사용
# from itertools import product
# n, m = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# res = sorted(list(set(product(arr, repeat=m))))
# for x in res:
#     print(*x)