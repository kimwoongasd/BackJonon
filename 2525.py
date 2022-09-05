a, b = map(int, input().split())
c = int(input())

total = b + c
mod = total % 60

if total >= 60:
    a += total // 60
    
if a >= 24:
    a -= 24

print(f"{a} {mod}")