import sys

n, m = map(int, sys.stdin.readline().split())
tem = list(map(int, sys.stdin.readline().split()))

number = [0]
s = 0
for i in range(n):
    s += tem[i]
    number.append(s)

for k in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(number[j] - number[i - 1])


# 시간초과
# n, m = map(int, input().split())
# tem = list(map(int, input().split()))

# for k in range(m):
#     i, j = map(int, input().split())
#     s = sum(tem[i - 1:j])
#     print(s)