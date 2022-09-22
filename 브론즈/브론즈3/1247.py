import sys

for _ in range(3):
    n = int(input())
    tem = 0
    s = 0
    for i in range(n):
        a = int(sys.stdin.readline())
        tem += a
        
    if tem == 0:
        s = "0"
    elif tem > 0:
        s = "+"
    else:
        s = "-"
    
    print(s)
