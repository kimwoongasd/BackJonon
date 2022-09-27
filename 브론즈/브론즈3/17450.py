name = []
for i in range(3):
    m, w = map(int, input().split())
    
    m *= 10
    w *= 10
    
    if m >= 5000:
        m -= 500
    
    money = w / m
    name.append(money)

res = max(name)
for i in range(3):
    if name[i] == res:
        if i == 0:
            print("S")
        elif i == 1:
            print("N")
        else:
            print("U")