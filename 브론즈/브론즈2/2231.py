n = int(input())

for i in range(1, n):
    tem = list(map(int, str(i)))
    s = i + sum(tem)
    
    if s == n:
        print(i)
        exit()
print(0)