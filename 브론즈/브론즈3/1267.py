n = int(input())
tem = list(map(int, input().split()))

x = 0
z = 0

for i in range(n):
    x += (tem[i] // 30) + 1
    z += (tem[i] // 60) + 1

y = x * 10
m = z * 15

    
if y > m:
    print(f"M {m}")
elif y == m:
    print(f"Y M {y}")
else:
    print(f"Y {y}")