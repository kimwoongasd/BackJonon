a, b, c = map(int, input().split())

res = 0

if a == b and b == c and c == b:
    res = 10000 + (a * 1000)

elif a == b and b != c:
    res = 1000 + (a * 100)
    
elif a != b and b == c:
    res = 1000 + (b * 100)
    
elif a == c and a != b:
    res = 1000 + (a * 100)

else:
    res = max(a, b, c) * 100
    
print(res)