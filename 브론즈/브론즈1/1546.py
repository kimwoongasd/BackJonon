n = int(input())
tem = list(map(int, input().split()))

max_tem = max(tem)
total = 0

for i in range(n):
    total += tem[i] / max_tem * 100

print(total / n)