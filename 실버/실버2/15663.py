def dfs(L):
    if L == m:
        print(*res)
    else:
        t = 0
        for i in range(n):
            if ch[i] == 0 and arr[i] != t:
                ch[i] = 1
                res[L] = arr[i]
                t = arr[i]
                dfs(L + 1)
                ch[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ch = [0] * n
res = [0] * m
dfs(0)

# itertools 사용
# from itertools import permutations
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# res = sorted(set(list(permutations(arr, m))))
# for x in res:
#     print(*x)