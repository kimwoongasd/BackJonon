def dfs(x, L):
    global ch, res, n
    if L == 6:
        print(*res)
        
    else:
        for i in range(x, n + 1):
            if ch[i] == 0:
                res[L] = tem[i]
                ch[i] = 1
                dfs(i, L + 1)
                ch[i] = 0

while True:
    tem = list(map(int, input().split()))
    n = tem[0]
    if tem[0] == 0:
        break
    
    else:
        ch = [0] * (n + 1)
        res = [0] * 6
        dfs(1, 0)
        print()
        
# 함수 사용
# from itertools import combinations

# while True:
#     tem = list(map(int, input().split()))
#     n = tem.pop(0)
#     if n == 0:
#         break
    
#     for x in combinations(tem, 6):
#         print(*x)
#     print()