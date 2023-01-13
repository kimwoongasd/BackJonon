import  sys
input = sys.stdin.readline
n = int(input())
tmp = list(map(int, input().split()))
stack = []
res = [-1] * n

for i in range(n):
    while stack and tmp[stack[-1]] < tmp[i]:
        res[stack.pop()] = tmp[i]
    stack.append(i)

print(*res)

# 시간초과
# n = int(input())
# arr = list(map(int, input().split()))
# res = [-1] * n

# for i in range(n - 1):
#     for j in range(i, n):
#         if arr[i] < arr[j]:
#             res[i] = arr[j]
#             break
# print(*res)