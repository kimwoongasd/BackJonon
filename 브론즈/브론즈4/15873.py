n = input()

res = 0
tem = 0
for x in n:
    if int(x) == 0:
        res -= tem
        tem *=10
        res += tem
        
    tem = int(x)
    res += int(x)
    
print(res)