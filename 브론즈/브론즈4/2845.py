L, P = map(int, input().split())
tem = list(map(int, input().split()))

total = L * P

for x in tem:
    print(x - total, end=" ")