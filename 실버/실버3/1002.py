import math
n = int(input())

for i in range(n):
    x_1, y_1, r_1, x_2, y_2, r_2 = map(int, input().split())
    
    d = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
    
    if d == 0:
        if r_1 == r_2:
            print(-1)
        else:
            print(0)
        
    else:
        if r_1 + r_2 == d or abs(r_2 - r_1) == d:
            print(1)
        elif abs(r_1 - r_2) < d < abs(r_1 + r_2):
            print(2)
        else:
            print(0)