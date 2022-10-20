n, m = map(int, input().split())
tem = list(map(int, input().split()))
count = 0
lt = 0
rt = 1

while rt <= n and lt <= rt:
    s = sum(tem[lt:rt])
    
    if s < m:
        rt += 1
    elif s > m:
        lt += 1
    else:
        count += 1
        rt += 1
print(count)

# 시간초과
# for i in range(n):
#     s = 0
#     for j in range(i, n):
#         s += tem[j]
#         if s == m:
#             count += 1
#             break
#         elif s > m:
#             break
# print(count)