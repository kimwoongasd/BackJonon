n = int(input())

for i in range(n):
    a = int(input())
    b = int(input())
    
    tem = [x for x in range(1, b + 1)]
    for j in range(a):
        for k in range(1, b):
            tem[k] += tem[k - 1]
    print(tem[-1])