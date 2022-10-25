import sys

n = int(sys.stdin.readline())
ls = []
for i in range(n):
    tem = list(map(str, sys.stdin.readline().split()))
    
    if tem[0] == "push":
        ls.append(tem[1])
    elif tem[0] == "pop":
        if ls:
            print(ls.pop())
        else:
            print(-1)
    elif tem[0] == "size":
        print(len(ls))
    elif tem[0] == "empty":
        if len(ls) == 0:
            print(1)
        else:
            print(0)
    else:
        if ls:
            print(ls[-1])
        else:
            print(-1)