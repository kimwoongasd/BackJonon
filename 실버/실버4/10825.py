import sys

n = int(input())
tem = []

for i in range(n):
    a, b, c, d = sys.stdin.readline().split()
    tem.append((a, b, c, d))

tem.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for x in tem:
    print(f"{x[0]}")