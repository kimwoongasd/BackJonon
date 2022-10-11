import sys
n = int(input())
tem = []

for i in range(n):
    a = sys.stdin.readline().strip()
    tem.append(a)

tem = set(tem)  
tem = sorted(tem)
tem.sort(key=len)

for x in tem:
    print(x)