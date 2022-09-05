a, b = map(int, input().split())
c = int(input())

m = 0
total = b + c
mod = total % 60

if total >= 60:
    a += total // 60
    
    if a >= 24:
        a = 0

print(f"{a} {mod}")