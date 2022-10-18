import sys
n = int(sys.stdin.readline())
tem = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    tem.append((a, b))

tem.sort(key=lambda x : (x[0], x[1]))
for x in tem:
    print(f"{x[0]} {x[1]}")