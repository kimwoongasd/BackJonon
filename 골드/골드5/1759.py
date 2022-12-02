def dfs(L, x, s):
    global res, ch, vowels
    if L == n:
        if 2 <= x < n:
            for x in res:
                print(x, end="")
            print()
    else:
        for i in range(s, m):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = arr[i]
                if arr[i] in vowels:
                    dfs(L + 1, x - 1, i + 1)
                else:
                    dfs(L + 1, x, i + 1)
                ch[i] = 0

n, m = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
ch = [0] * m
vowels = ["a", "e", "i", "o", "u"]
res = [0] * n
dfs(0, n, 0)