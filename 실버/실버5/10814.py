n = int(input())
tem = []
for i in range(n):
    a, b = map(str, input().split())
    tem.append((a, b, i + 1))
  
tem.sort(key=lambda x: (int(x[0]), x[2]))

for x in tem:
    print(f"{x[0]} {x[1]}")