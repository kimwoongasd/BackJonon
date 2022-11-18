# pyp3로 풀림
import sys
sys.setrecursionlimit(10**6)
def dfs(L, s):
    global res
    if L == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if ch[i] == 0 and ch[j] == 0:
                    start += arr[i][j]
                elif ch[i] == 1 and ch[j] == 1:
                    link += arr[i][j]
        if res > abs(start - link):
            res = abs(start - link)
        
    else:
        for i in range(s, n):
            if ch[i] == 0:
                ch[i] = 1
                dfs(L + 1, i + 1)
                ch[i] = 0


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a = list(map(int ,sys.stdin.readline().split()))
    arr.append(a)
ch = [0] * n
res = 2147000000
dfs(0, 0)
print(res)