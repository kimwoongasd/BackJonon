import sys
n, m = map(int, sys.stdin.readline().split())

a = set()
b = set()
for i in range(n):
    a.add(sys.stdin.readline())
    
for j in range(m):
    b.add(sys.stdin.readline())
res = sorted(list(a & b))

print(len(res))
for x in res:
    print(x)

# 시간초과
# a = []
# b = []
# for i in range(n):
#     a.append(input())

# for j in range(m):
#     b.append(input())
# c = []
# if n > m:
#     for i in range(n):
#         if a[i] in b:
#             c.append(a[i])
# else:
#     for i in range(m):
#         if b[i] in a:
#             c.append(b[i])

# c.sort()
# print(len(c))
# for x in c:
#     print(x)
