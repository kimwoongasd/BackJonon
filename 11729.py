def hanoi_top(n, a, b, c):
    if n == 1:
        print(a, c)
    
    else:
        hanoi_top(n - 1, a, c, b)
        print(a, c)
        hanoi_top(n - 1, b, a, c)
    

n = int(input())
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi_top(n, 1, 2, 3)