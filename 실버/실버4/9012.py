n = int(input())

for i in range(n):
    tem = input()
    
    ch = []
    for i in range(len(tem)):
        if tem[i] == "(":
            ch.append("(")
        else:
            if ch:
                ch.pop()
            else:
                print("NO")
                break
            
    else:
        if len(ch) == 0:
            print("YES")
        else:
            print("NO")