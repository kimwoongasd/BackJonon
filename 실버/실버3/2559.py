import sys
n, k = map(int, sys.stdin.readline().split())
tem = list(map(int, sys.stdin.readline().split()))

res = []
res.append(sum(tem[:k]))

for i in range(n - k):
    res.append(res[-1] - tem[i] + tem[i + k])

print(max(res))

# 시간초과 2
# res = []
# lt = 0
# rt = k

# while rt <= n:
#     res.append(sum(tem[lt:rt]))
#     lt += 1
#     rt += 1
# print(max(res))

# 시간초과
# res = 0
# lt = 0
# rt = k

# while rt <= n:
#     res = max(res, sum(tem[lt:rt]))
#     lt += 1
#     rt += 1
# print(res)