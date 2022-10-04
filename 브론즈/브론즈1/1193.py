n = int(input())

count = 0
s = 0
while s < n:
    count += 1
    s += count
    
gap = s - n

if count % 2 == 0:
    a = count - gap
    b = gap + 1
else:
    a = gap + 1
    b = count - gap
    
print(f"{a}/{b}")