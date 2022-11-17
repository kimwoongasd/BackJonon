def dfs(L):
    global num, ch, res
    if L == n:
        t = 0
        for i in range(n - 1):
            t += abs(num[i] - num[i + 1])
        if t > res:
            res = t
        
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                num[L] = tem[i]
                dfs(L + 1)
                ch[i] = 0

n = int(input())
tem = list(map(int, input().split()))
ch = [0] * n
num = [0] * n
res = 0
dfs(0)
print(res)