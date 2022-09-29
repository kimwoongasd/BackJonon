n = int(input())

res = 1
while n > 1:
    n -= (6 * res)
    res += 1
    
print(res)