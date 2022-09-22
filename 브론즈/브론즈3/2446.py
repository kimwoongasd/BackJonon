n = int(input())

for i in range(n , 0, -1):
    print(" " * (n - i) + "*" * (i * 2 - 1) + " " * (n - i))
    
for j in range(2, n + 1):
    print(" " * (n - j) + "*" * (j * 2 - 1)+ " " * (n - j))
    