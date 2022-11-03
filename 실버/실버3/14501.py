import time
start = time.time()
def dfs(x, s):
    global res
    if x > n:
        return
    elif x == n:
        if s > res:
            res = s
    else:
        dfs(x + tem[x][0], s + tem[x][1])
        dfs(x + 1, s)

n = int(input())
tem = []
res = 0
for i in range(n):
    t, p = map(int, input().split())
    tem.append((t, p))
dfs(0, 0)
print(res)
end = time.time()
print(f"{end - start:.5f} sec")

# 아래 코드가 시간 더 짧게 걸린다.
# 재귀는 시간이 오래 걸림
# n = int(input())

# ch = [0] * (n + 1)
# t_list = []
# p_list = []
# for i in range(n):
#     t, p = map(int, input().split())
#     t_list.append(t)
#     p_list.append(p)

# for i in range(n-1, -1, -1):
#     if i + t_list[i] > n:
#         ch[i] = ch[i + 1]
#     else:
#         ch[i] = max(ch[i + 1], p_list[i] + ch[i + t_list[i]])

# print(ch[0])